# -*- coding: utf-8 -*-

"""
Provide classes and functions to interact with Bluetooth LE devices.
"""

import struct
import socket
import binascii
import logging
import pathlib
import pickle
import time

from typing import Sequence, Optional, Set, Any, Type

from .hci_constants import ScanType, AddressType, FilterPolicy, \
    HCI_MAX_EVENT_SIZE, PacketType, Event, LeEvent, AdType, \
    CompanyId, DiscoveryType, ALL_16BIT_SERVICES
from .bluez_ffi import hci_get_route, hci_le_set_scan_parameters, \
    hci_le_set_scan_enable


class Advertisement(object):
    """
    Describes a single Bluetooth Low Energy Advertisement data block, 
    as described in the Bluetooth Core specification.
    """
    def analyse(self) -> None:
        """
        Analyse the Advertisement data block. Currently is capable of
        determining the device vendor and the offered services.
        """
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
                 svcs: Set[int] = set()) -> None:
        self.type = ad_type
        self.data = ad_data
        self.vendor = vendor
        self.services = svcs

    def __hash__(self) -> int:
        return hash(self.type) + hash(self.data)

    def __str__(self) -> str:
        if self.type is AdType.ManufacturerSpecificData and self.vendor is not None:
            return "[{}:{}:{}]".format(self.vendor.name, self.type.name, binascii.hexlify(self.data).decode("ascii"))
        elif self.type in (AdType.CompleteListOf16BitServiceClassUUIDs, AdType.IncompleteListOf16BitServiceClassUUIDs) and len(self.services) > 0:
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
    """
    This is the logical equivalent of the le_advertising_report structure
    in BlueZ.
    """
    @classmethod
    def create(cls, packet: bytes, offset: int = 0) -> "AdvertisementPacket":
        """
        Given a packet buffer and a starting offset, extract an 
        AdvertisementPacket.
        """
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

    def __init__(self,
                 dtype: DiscoveryType,
                 atype: AddressType,
                 addr: bytes,
                 rssi: int,
                 ads: Sequence[Advertisement]
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


class Device(object):
    """
    Identifies a Bluetooth Low Energy device.
    """
    def union(self, other: "Device") -> bool:
        """
        Perform an in-place union of the given device and self.
        """
        if isinstance(other, Device):
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
        else:
            raise TypeError("Expected a Device, got '{}'.".format(type(other)))

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
        addr_str = {binascii.hexlify(e).decode("ascii") for e in self.addresses}

        return "<Device: {} ({})>".format(addr_str, self.discovery_type.name)

    def __repr__(self):
        if self.vendor is None:
            vendor_str = "Unknown"
        else:
            vendor_str = self.vendor.name

        addr_str = {binascii.hexlify(e).decode("ascii") for e in self.addresses}

        return "<{}: {}, {}>".format(vendor_str, addr_str, self.advertisements)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Device):
            shared_addrs = len(self.addresses & other.addresses) > 0
            same_vendor = (self.vendor is not None) and (self.vendor is other.vendor)
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
            t: float = time.monotonic()
            while True:
                new_t: float = time.monotonic()
                packet = self._sock.recv(HCI_MAX_EVENT_SIZE)
                advert = self._parse_packet(packet)
                if advert is not None:
                    device = self._analyse_advert(advert)
                    self._register_device(device)

                if abs(new_t - t) >= self.backup_interval:
                    t = new_t
                    self._backup_registry()
        else:
            raise ValueError("You must use HciParser as context manager before calling HciParser.run().")

    def _find_device(self, device: Device) -> Optional[int]:
        """
        Determine the location of the given Device in the registry, or return
        None.
        """
        for idx, rd in enumerate(self.registry):
            if device == rd:
                return idx
        else:
            return None

    def _register_device(self, device: Device) -> None:
        """
        Given a Device, add it to the registry if it is not known, or update
        the existing Device(s) with the new data if a match was found.
        """
        if len(self.registry) > 0:
            idx = self._find_device(device)
            if idx is None:
                self._log.info("New device: {}".format(device))
                self._log.debug("Full info: {!r}".format(device))
                self.registry.append(device)
            elif self.registry[idx].union(device):
                self._log.info("Device update: {}".format(self.registry[idx]))
                self._log.debug("Full info: {!r}".format(self.registry[idx]))
        else:
            self._log.info("New device: {}".format(device))
            self._log.debug("Full info: {!r}".format(device))
            self.registry.append(device)

    def _backup_registry(self) -> None:
        """
        If the backup path is set, dump the registry object to a Pickle backup.
        """
        if self.backup_path is not None:
            self._log.debug("Writing backup dump.")
            with self.backup_path.open("wb") as f:
                pickle.dump(self.registry, f, pickle.HIGHEST_PROTOCOL)

    def _parse_packet(self, packet: bytes) -> Optional[AdvertisementPacket]:
        """
        Parse the next packet in the socket.
        """
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
        for ad_block in advert.advertisements:
            ad_block.analyse()
            device.vendor = ad_block.vendor
            device.services |= ad_block.services
            device.advertisements.add(ad_block)

        return device

    def __init__(self, bkp_path: Optional[pathlib.Path] = None, backup_interval: float = 60.0) -> None:
        self.backup_path = bkp_path
        self.backup_interval = backup_interval
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
