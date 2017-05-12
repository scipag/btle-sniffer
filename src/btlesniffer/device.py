# -*- coding: utf-8 -*-

"""
Provides the Device abstraction of a Bluetooth device akin to org.bluez.Device1.
"""

import datetime
from typing import Dict, Any, Optional, Sequence, MutableMapping

from .hci_constants import CompanyId, uuid_to_string


class GATTDescriptor(object):
    def __init__(self, uuid: str, value: Optional[Sequence[int]],
                 flags: Sequence[str]):
        self.uuid = uuid
        self.value = value
        self.flags = flags


class GATTCharacteristic(object):
    def __init__(self, uuid: str, value: Optional[Sequence[int]],
                 flags: Sequence[str]):
        self.uuid = uuid
        self.value = value
        self.flags = flags
        self.descriptors: MutableMapping[str, GATTDescriptor] = dict()

    def __getitem__(self, path: str) -> GATTDescriptor:
        return self.descriptors[path]

    def __setitem__(self, path: str, descriptor: GATTDescriptor):
        self.descriptors[path] = descriptor


class GATTService(object):
    def __init__(self, uuid: str, primary: bool):
        self.uuid = uuid
        self.primary = primary
        self.characteristics: MutableMapping[str, GATTCharacteristic] = dict()

    def __getitem__(self, path: str) -> GATTCharacteristic:
        return self.characteristics[path]

    def __setitem__(self, path: str, characteristic: GATTCharacteristic):
        self.characteristics[path] = characteristic


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
            self.uuids = self.uuids.union(data["ServiceData"].keys())
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
        self.uuids = self.uuids.union(device.service_data.keys())
        self.rssis.extend(device.rssis)
        if device.tx_power is not None:
            self.tx_power = device.tx_power
        self.last_seen = device.last_seen
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
        self.services: MutableMapping[str, GATTService] = dict()

        self.manufacturer_data = dict()
        if manufacturer_data is not None:
            for k, v in manufacturer_data.items():
                self.manufacturer_data[k] = [v]

        self.service_data = dict()
        if service_data is not None:
            self.uuids = self.uuids.union(service_data.keys())
            for k, v in service_data.items():
                self.service_data[k] = [v]

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Device):
            return self.address == other.address
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

        uuids = list()
        for u in self.uuids:
            text = uuid_to_string(u)
            if text is not None:
                uuids.append(text)
        if len(uuids) > 0:
            uuid_str = "; Services: {}".format(", ".join(uuids))
        else:
            uuid_str = ""

        return "{}; {} ({} dBa){}{}".format(
            name, self.address, rssi, vendor_str, uuid_str
        )

    def __getitem__(self, path: str) -> GATTService:
        return self.services[path]

    def __setitem__(self, path: str, service: GATTService):
        self.services[path] = service


def print_device(device, prefix=None):
    if prefix is not None:
        print("{}: {!s}".format(prefix, device))
    else:
        print("{!s}".format(device))
