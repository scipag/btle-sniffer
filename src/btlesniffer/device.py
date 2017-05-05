# -*- coding: utf-8 -*-

"""
Provides the Device abstraction of a Bluetooth device akin to org.bluez.Device1.
"""

import datetime
from typing import Dict, Any, Optional, Sequence

from .hci_constants import CompanyId, uuid_to_string


class Device(object):
    @classmethod
    def create_from_dbus_dict(cls, path: str, data: Dict[str, Any]) -> "Device":
        return cls(
            path,
            data["Address"],
            data["Paired"],
            data["Connected"],
            data["ServicesResolved"],
            data.get("Name", None),
            data.get("Class", None),
            data.get("Appearance", None),
            data.get("UUIDs", list()),
            data.get("RSSI", None),
            data.get("TxPower", None),
            data.get("ManufacturerData", dict()),
            data.get("ServiceData", dict())
        )

    def update_from_dbus_dict(self, path: str, data: Dict[str, Any]) -> None:
        self.last_seen = datetime.datetime.now()
        self.path = path
        if "Address" in data:
            self.address = data["Address"]
        if "Paired" in data:
            self.paired = data["Paired"]
        if "Connected" in data:
            self.connected = data["Connected"]
        if "ServicesResolved" in data:
            self.services_resolved = data["ServicesResolved"]
        if "Name" in data:
            self.name = data["Name"]
        if "Class" in data:
            self.device_class = data["Class"]
        if "Appearance" in data:
            self.appearance = data["Appearance"]
        if "UUIDs" in data:
            self.uuids = self.uuids.union(data["UUIDs"])
        if "RSSI" in data:
            self.rssis.append(data["RSSI"])
        if "TxPower" in data:
            self.tx_power = data["TxPower"]
        if "ManufacturerData" in data:
            for k, v in data["ManufacturerData"].items():
                if k in self.manufacturer_data:
                    self.manufacturer_data[k].append(v)
                else:
                    self.manufacturer_data[k] = [v]
        if "ServiceData" in data:
            self.services = self.services.union(data["ServiceData"].keys())
            for k, v in data["ServiceData"].items():
                if k in self.service_data:
                    self.service_data[k].append(v)
                else:
                    self.service_data[k] = [v]

    def update_from_device(self, device: "Device") -> None:
        self.path = device.path
        self.address = device.address
        self.paired |= device.paired
        self.connected |= device.connected
        self.services_resolved |= device.services_resolved
        if device.name is not None:
            self.name = device.name
        if device.device_class is not None:
            self.device_class = device.device_class
        if device.appearance is not None:
            self.appearance = device.appearance
        self.uuids |= device.uuids
        self.rssis.extend(device.rssis)
        if device.tx_power is not None:
            self.tx_power = device.tx_power
        self.last_seen = device.last_seen
        self.services = self.services.union(device.services)
        self.services = self.services.union(device.service_data.keys())
        for k, v in device.manufacturer_data.items():
            if k in self.manufacturer_data:
                self.manufacturer_data[k].extend(v)
            else:
                self.manufacturer_data[k] = v

        for k, v in device.service_data.items():
            if k in self.service_data:
                self.service_data[k].extend(v)
            else:
                self.service_data[k] = v

    def mark_inactive(self):
        self.active = False

    def add_service(self, service):
        self.uuids.add(service)

    def __init__(self,
                 path: str, address: str,
                 paired: bool, connected: bool, services_resolved: bool,
                 name: Optional[str] = None, device_class: Optional[int] = None,
                 appearance: Optional[int] = None, uuids: Sequence[str] = None,
                 rssi: int = None, tx_power: int = None,
                 manufacturer_data: Dict[int, Sequence[int]] = None,
                 service_data: Dict[str, Sequence[int]] = None) -> None:
        self.active = True
        self.path = path
        self.address = address
        self.paired = paired
        self.connected = connected
        self.services_resolved = services_resolved
        self.name = name
        self.device_class = device_class
        self.appearance = appearance
        self.uuids = set(uuids) if uuids is not None else set()
        self.rssis = [rssi] if rssi is not None else list()
        self.tx_power = tx_power
        self.first_seen = datetime.datetime.now()
        self.last_seen = datetime.datetime.now()
        self.services = set()

        self.manufacturer_data = dict()
        if manufacturer_data is not None:
            for k, v in manufacturer_data.items():
                self.manufacturer_data[k] = [v]

        self.service_data = dict()
        if service_data is not None:
            self.services = self.services.union(service_data.keys())
            for k, v in service_data.items():
                self.service_data[k] = [v]

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Device):
            shared_addrs = self.address == other.address
            same_name = self.name is not None and self.name == other.name
            same_class = self.device_class is not None and self.device_class == other.device_class
            same_appearance = self.appearance is not None and self.appearance == other.appearance
            same_vendors = len(self.manufacturer_data) > 0 and self.manufacturer_data.keys() == other.manufacturer_data.keys()
            same_services = len(self.service_data) > 0 and self.service_data.keys() == other.service_data.keys()
            # return (shared_addrs or same_name or same_class or same_appearance) and (same_vendors or same_services)
            return shared_addrs
        else:
            return NotImplemented

    def __str__(self) -> str:
        name = self.name if self.name is not None else "Unknown"
        rssi = self.rssis[-1] if len(self.rssis) > 0 else -120
        vendors = list()
        for k in self.manufacturer_data.keys():
            try:
                vendors.append(CompanyId(k).name)
            except ValueError:
                vendors.append(str(k))
        if len(vendors) > 0:
            vendor_str = "; Vendors: {}".format(", ".join(vendors))
        else:
            vendor_str = ""

        services = list()
        for u in self.services:
            text = uuid_to_string(u)
            if text is not None:
                services.append(text)
        if len(services) > 0:
            service_str = "; Services: {}".format(", ".join(services))
        else:
            service_str = ""

        return "{}; {} ({} dBa){}{}".format(
            name, self.address, rssi, vendor_str, service_str
        )

        # return "Device:\n" \
        #        "  Active: {}, Adresses: {},\n" \
        #        "  Paired: {}, Connected: {},\n" \
        #        "  Name: {}, Device Class: {}, Appearance: {}\n" \
        #        "  First Seen: {}, Last Seen: {}\n" \
        #        "  RSSI: {},\n" \
        #        "  Manufacturer Data Packets: {}, Known Vendors: {},\n" \
        #        "  Known Services or Characteristics: {}".format(
        #     self.active,
        #     self.addresses, self.paired, self.connected,
        #     name, device_class, appearance, self.first_seen.isoformat(),
        #     self.last_seen.isoformat(), rssi, num_man_fac_pkts,
        #     ", ".join(vendors), ", ".join(uuids))


def print_device(device, prefix=None):
    if device.active:
        if prefix is not None:
            print("{}: {!s}".format(prefix, device))
        else:
            print("{!s}".format(device))

