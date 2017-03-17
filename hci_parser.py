# -*- coding: utf-8 -*-

"""
Provide classes and functions to interact with Bluetooth LE devices.
"""

import struct
import socket
import contextlib
import binascii
import datetime
import logging
import pathlib

from typing import Tuple, Optional, Set, Any, Type

from hci_constants import ScanType, AddressType, FilterPolicy, HCI_MAX_EVENT_SIZE, \
    PacketType, Event, LeEvent, AdType, CompanyId, DiscoveryType, ALL_16BIT_SERVICES
from bluez_ffi import hci_get_route, hci_le_set_scan_parameters, hci_le_set_scan_enable


class Advertisement(object):
    def analyse(self) -> None:
        if self.type is AdType.ManufacturerSpecificData:
            vendor, data = struct.unpack("<H{}s".format(len(self.data) - 2), self.data)
            self.vendor = CompanyId(vendor)
        elif self.type in (AdType.CompleteListOf16BitServiceClassUUIDs, AdType.IncompleteListOf16BitServiceClassUUIDs):
            service_count = len(self.data) // 2
            self.services = set(struct.unpack("<{}H".format(service_count), self.data))

    def __init__(self, 
                 ad_type: AdType, 
                 ad_data: bytes, 
                 vendor: Optional[CompanyId] = None,
                 svcs: Optional[Set[int]] = None) -> None:
        self.type: AdType = ad_type
        self.data: bytes = ad_data
        self.vendor: Optional[CompanyId] = vendor
        self.services: Optional[Set[int]] = svcs

    def __hash__(self) -> int:
        return hash(self.type) + hash(self.data)

    def __str__(self) -> str:
        if self.type is AdType.ManufacturerSpecificData and self.vendor is not None:
            return "[{}:{}:{}]".format(self.vendor.name, self.type.name, binascii.hexlify(self.data).decode("ascii"))
        elif self.type in (AdType.CompleteListOf16BitServiceClassUUIDs, AdType.IncompleteListOf16BitServiceClassUUIDs) and self.services is not None:
            return "[{}:{}]".format(self.type.name, [ALL_16BIT_SERVICES.get(s, s) for s in self.services])
        else:
            return "[{}:{}]".format(self.type.name, binascii.hexlify(self.data).decode("ascii"))

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Advertisement):
            return self.type is other.type and self.data == other.data
        else:
            return NotImplemented


class AdvertisementPacket(object):
    def __init__(self, 
                 dtype: DiscoveryType, 
                 atype: AddressType, 
                 addr: bytes, 
                 rssi: int, 
                 ads: Tuple[Advertisement, ...]
                 ) -> None:
        self.discovery_type = dtype
        self.address_type = atype
        self.address = addr
        self.rssi = rssi,
        self.advertisements = ads

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, AdvertisementPacket):
            return self.discovery_type is other.discovery_type \
                and self.address_type is other.address_type \
                and self.address == other.address \
                and self.advertisements == other.advertisements
        else:
            return NotImplemented

    @classmethod
    def create(cls, packet: bytes, offset: int = 0) -> "AdvertisementPacket":
        report_header = struct.unpack_from(">BB7sB", packet, offset)
        discovery_type = DiscoveryType(report_header[0])
        address_type = AddressType(report_header[1])
        address = report_header[2]
        ad_data_length = report_header[3]

        report_body = struct.unpack_from(">{}sb".format(ad_data_length), packet, offset + 10)
        report_data = report_body[0]
        rssi = report_body[1]

        advertisements = list()

        i = 0
        while i < len(report_data):
            ad_length = report_data[i]
            ad_type = AdType(report_data[i + 1])
            advertisements.append(
                Advertisement(ad_type, report_data[i + 2:i + 1 + ad_length])
            )
            i += ad_length + 1

        return cls(
            discovery_type,
            address_type,
            address,
            rssi,
            tuple(advertisements)
        )


class Device(object):
    def union(self, other: "Device") -> bool:
        if self.vendor is other.vendor:
            new_addrs = self.addresses | other.addresses
            new_svcs = self.services | other.services
            new_ads = self.advertisements | other.advertisements

            if new_addrs == self.addresses and new_svcs == self.services and new_ads == self.advertisements:
                return False
            else:
                self.addresses = new_addrs
                self.services = new_svcs
                self.advertisements = new_ads
                return True
        else:
            raise ValueError("The two devices do not have the same vendor.")

    def __init__(self, 
                 dtype: DiscoveryType, 
                 atype: AddressType, 
                 addrs: Set[bytes],
                 vendor: Optional[CompanyId] = None,
                 svcs: set = set(),
                 ads: Set[Advertisement] = set()) -> None:
        self.discovery_type = dtype
        self.address_type = atype
        self.addresses = addrs
        self.vendor = vendor
        self.services = svcs
        self.advertisements = ads

    def __str__(self) -> str:
        if self.vendor is None:
            vendor_str = "Unknown"
        else:
            vendor_str = self.vendor.name

        addr_str = {binascii.hexlify(e).decode("ascii") for e in self.addresses}

        return "<{}: {}, {}>".format(vendor_str, addr_str, self.advertisements)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Device):
            shared_addrs = len(self.addresses & other.addresses) > 0
            same_vendor = self.vendor is other.vendor
            same_services = len(self.services) > 0 and self.services >= other.services
            same_advertisements = len(self.advertisements) > 0 and self.advertisements >= other.advertisements
            return shared_addrs or (same_vendor and (same_services or same_advertisements))
        else:
            return NotImplemented


class HciParser(object):
    """
    HciParser implements a context manager that can scan for BTLE devices,
    and maintain a database of the recognised devices.
    """
    def run(self) -> None:
        """
        Run the main discovery loop.
        """
        if self._sock is not None:
            iterations: int = 0
            while True:
                packet = self._sock.recv(HCI_MAX_EVENT_SIZE)
                advert = self._parse_packet(packet)
                if advert is not None:
                    device = self._analyse_advert(advert)
                    self._register_device(device)

                # if iterations % 50 == 0:
                #     self._backup_registry()

                iterations += 1
        else:
            raise ValueError("You must use HciParser as context manager before calling HciParser.run().")

    def _find_device(self, device: Device) -> Optional[int]:
        if device in self.registry:
            return self.registry.index(device)
        else:
            return None

    def _register_device(self, device: Device) -> None:
        if len(self.registry) > 0:
            idx = self._find_device(device)
            if idx is None:
                self._log.info("{}".format(device))
                self.registry.append(device)
            elif self.registry[idx].union(device):
                self._log.info("Device update: {}".format(self.registry[idx]))
        else:
            self._log.info("{}".format(device))
            self.registry.append(device)

    def _backup_registry(self) -> None:
        if self.backup_path is not None:
            pass

    def _parse_packet(self, packet: bytes) -> Optional[AdvertisementPacket]:
        """
        Parse the next packet in the socket.
        """
        self._log.debug("Raw: {}".format(binascii.hexlify(packet).decode("ascii")))
        if packet[0] == PacketType.Event and packet[1] == Event.Le and packet[3] == LeEvent.LeAdvertisingReport:
            return AdvertisementPacket.create(packet, 4)

        return None

    def _analyse_advert(self, advert: AdvertisementPacket) -> Device:
        """
        Analyse the content of the specified advertisement packet.
        """
        device = Device(
            advert.discovery_type, 
            advert.address_type, 
            {advert.address}
        )
        ad_str = list()
        for ad_block in advert.advertisements:
            if ad_block.type is AdType.ManufacturerSpecificData:
                vendor, data = struct.unpack("<H{}s".format(len(ad_block.data) - 2), ad_block.data)
                vendor = CompanyId(vendor)
                device.vendor = vendor
                ad_str.append("[{}:{}:{}]".format(vendor.name, ad_block.type.name, binascii.hexlify(ad_block.data).decode("ascii")))
            elif ad_block.type in (AdType.CompleteListOf16BitServiceClassUUIDs, AdType.IncompleteListOf16BitServiceClassUUIDs):
                service_count = len(ad_block.data) // 2
                services = struct.unpack("<{}H".format(service_count), ad_block.data)
                device.services.add(services)
                ad_str.append("[{}:{}]".format(ad_block.type.name, services))
            else:
                device.advertisements.add(ad_block)
                ad_str.append("[{}:{}]".format(ad_block.type.name, binascii.hexlify(ad_block.data).decode("ascii")))

        self._log.debug("".join(ad_str))

        return device

    def __init__(self, bkp_path: Optional[pathlib.Path] = None) -> None:
        self.backup_path: Optional[pathlib.Path] = bkp_path
        self.registry: list = list()
        self._sock: Optional[socket.socket] = None
        self._log: logging.Logger = logging.getLogger(__name__)

    def __enter__(self) -> "HciParser":
        required_constants = ("AF_BLUETOOTH", "BTPROTO_HCI", "SOL_HCI", "HCI_FILTER")
        if not all(hasattr(socket, a) for a in required_constants):
            raise RuntimeError("The current system does not support Unix Bluetooth sockets.")

        dev_id = hci_get_route()
        self._sock = socket.socket(
            socket.AF_BLUETOOTH,
            socket.SOCK_RAW,
            socket.BTPROTO_HCI
        )
        self._sock.bind((dev_id,))

        hci_le_set_scan_parameters(
            self._sock,
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
        self._sock.setsockopt(socket.SOL_HCI, socket.HCI_FILTER, hci_filter)

        hci_le_set_scan_enable(self._sock, True, False, 2000)

        return self

    def __exit__(self, 
                 exc_type: Optional[Type[Exception]], 
                 exc_val: Optional[Exception], 
                 trcbak: Any) -> bool:
        if self._sock is not None:
            hci_le_set_scan_enable(self._sock, False, False, 2000)
            self._sock.close()
            self._sock = None
        return False
