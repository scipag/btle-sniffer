#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import struct
import socket
import contextlib
import binascii
import datetime

from hci_constants import ScanType, AddressType, FilterPolicy, hci_max_event_size, PacketType, Event, LeEvent, \
    AdType, CompanyId, DiscoveryType, All16BitServices
from bluez_ffi import hci_get_route, hci_le_set_scan_parameters, hci_le_set_scan_enable


@contextlib.contextmanager
def setup_socket():
    if not all(hasattr(socket, a) for a in ("AF_BLUETOOTH", "BTPROTO_HCI", "SOL_HCI", "HCI_FILTER")):
        raise RuntimeError("The current system does not support Unix Bluetooth sockets.")

    dev_id = hci_get_route()
    sock = socket.socket(
            socket.AF_BLUETOOTH,
            socket.SOCK_RAW,
            socket.BTPROTO_HCI
            )
    sock.bind((dev_id,))

    hci_le_set_scan_parameters(
        sock,
        ScanType.PassiveScan,
        0x0010,
        0x0010,
        AddressType.PublicDeviceAddress,
        FilterPolicy.UndirectedAdsOnly,
        2000
    )

    hci_filter = struct.pack(
        "<IQH",
        0x00000010,
        0x4000000000000000,
        0x0000
    )
    sock.setsockopt(socket.SOL_HCI, socket.HCI_FILTER, hci_filter)

    hci_le_set_scan_enable(sock, True, False, 2000)

    yield sock

    hci_le_set_scan_enable(sock, False, False, 2000)

    sock.close()


def main():
    if os.geteuid() != 0:
        raise PermissionError("You must be root to run this program.")

    device_registry = list()

    with setup_socket() as sock:
        while True:
            d = sock.recv(hci_max_event_size)
            # print("Raw: {}".format(binascii.hexlify(d).decode("ascii")))

            packet_type = PacketType(d[0])
            if packet_type is PacketType.Event:
                event_type = Event(d[1])
                if event_type is Event.Le:
                    parameter_length = d[2]
                    sub_event = LeEvent(d[3])
                    if sub_event is LeEvent.LeAdvertisingReport:
                        timestamp = datetime.datetime.now()

                        report_header = struct.unpack_from(">BB7sB", d, 4)
                        discovery_type = DiscoveryType(report_header[0])
                        address_type = AddressType(report_header[1])
                        address = binascii.hexlify(report_header[2]).decode("ascii")
                        ad_data_length = report_header[3]

                        report_body = struct.unpack_from(">{}sb".format(ad_data_length), d, 14)
                        report_data = report_body[0]
                        rssi = report_body[1]

                        advertisements = list()

                        i = 0
                        while i < len(report_data):
                            ad_length = report_data[i]
                            ad_type = AdType(report_data[i + 1])

                            if ad_type is AdType.ManufacturerSpecificData:
                                ad = struct.unpack_from("<H{}s".format(ad_length - 3), report_data, i + 2)
                                ad_vendor = CompanyId(ad[0])
                                ad_data = binascii.hexlify(ad[1]).decode("ascii")
                                advertisements.append({"vendor": ad_vendor, "type": ad_type, "data": ad_data})
                            elif ad_type is AdType.CompleteListOf16BitServiceClassUUIDs:
                                service_count = (ad_length - 1) // 2
                                services = struct.unpack_from("<{}H".format(service_count), report_data, i + 2)
                                advertisements.append({"type": ad_type, "services": [All16BitServices.get(s, s) for s in services]})
                            else:
                                ad = struct.unpack_from("<{}s".format(ad_length - 1), report_data, i + 2)
                                ad_data = binascii.hexlify(ad[0]).decode("ascii")
                                advertisements.append({"type": ad_type, "data": ad_data})

                            i += ad_length + 1

                        ads_str = list()
                        for a in advertisements:
                            if "vendor" in a:
                                ads_str.append("[{}:{}:{}]".format(a["vendor"].name, a["type"].name, a["data"]))
                            elif "services" in a:
                                ads_str.append("[{}:{}]".format(a["type"].name, a["services"]))
                            else:
                                ads_str.append("[{}:{}]".format(a["type"].name, a["data"]))

                        analyzed_packet = {
                            "timestamp": timestamp,
                            "discovery_type": discovery_type,
                            "address_type": address_type,
                            "address": address,
                            "rssi": rssi,
                            "advertisements": advertisements
                        }

                        if len(device_registry) > 0:
                            known_addresses = [e["address"] for e in device_registry]
                            if address in known_addresses:
                                device_id = known_addresses.index(address)
                            else:
                                print("{}, {} - {} dBa, {}".format(address, "".join(ads_str), rssi, discovery_type.name))
                                device_registry.append(analyzed_packet)
                        else:
                            print("{}, {} - {} dBa, {}".format(address, "".join(ads_str), rssi, discovery_type.name))
                            device_registry.append(analyzed_packet)


if __name__ == "__main__":
    main()
