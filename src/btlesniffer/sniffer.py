# -*- coding: utf-8 -*-

"""
Provide a class that uses the D-Bus API of BlueZ to capture nearby Bluetooth
devices.
"""

import logging
import pickle
import datetime

import pydbus
from gi.repository import GLib

from .hci_constants import CompanyId
from .util import SERVICE_NAME, DEVICE_INTERFACE, OBJECT_MANAGER_INTERFACE, \
    PROPERTIES_INTERFACE, find_adapter


class Device(object):
    @classmethod
    def create_from_dbus_dict(cls, path, data):
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

    def update_from_dbus_dict(self, path, data):
        self.last_seen = datetime.datetime.now()
        self.paths.add(path)
        if "Address" in data:
            self.addresses.add(data["Address"])
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
            for k, v in data["ServiceData"].items():
                if k in self.service_data:
                    self.service_data[k].append(v)
                else:
                    self.service_data[k] = [v]

    def __init__(self, path, address, paired, connected, services_resolved,
                 name=None, device_class=None, appearance=None,
                 uuids=None, rssi=None, tx_power=None, manufacturer_data=None,
                 service_data=None):
        self.paths = {path}
        self.addresses = {address}
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

        self.manufacturer_data = dict()
        if manufacturer_data is not None:
            for k, v in manufacturer_data.items():
                self.manufacturer_data[k] = [v]

        self.service_data = dict()
        if service_data is not None:
            for k, v in service_data.items():
                self.service_data[k] = [v]

    def __repr__(self):
        return "{}{}".format(self.__class__.__name__, (
            self.paths, self.addresses, self.paired, self.connected,
            self.services_resolved, self.name, self.device_class,
            self.appearance, self.uuids, self.rssis, self.tx_power,
            self.first_seen, self.last_seen,
            self.manufacturer_data, self.service_data
        ))

    def __str__(self):
        name = self.name if self.name is not None else "Unknown"
        device_class = self.device_class if self.device_class is not None else "Unknown"
        appearance = self.appearance if self.appearance is not None else "Unknown"
        num_man_fac_pkts = sum(len(v) for v in self.manufacturer_data.values())
        vendors = ", ".join(CompanyId(k).name for k in self.manufacturer_data.keys())
        return "Device:\n" \
               "  Adresses: {},\n" \
               "  Paired: {}, Connected: {},\n" \
               "  Name: {}, Device Class: {}, Appearance: {}\n" \
               "  Number of Services: {}, Services Resolved: {}\n" \
               "  First Seen: {}, Last Seen: {}\n" \
               "  RSSI: {},\n" \
               "  Manufacturer Data Packets: {}, Known Vendors: {},\n" \
               "  Service Data: {}".format(
            self.addresses, self.paired, self.connected,
            name, device_class, appearance, len(self.uuids),
            self.services_resolved, self.first_seen.isoformat(), self.last_seen.isoformat(),
            self.rssis[-1], num_man_fac_pkts, vendors, self.service_data)


class Sniffer(object):
    """
    Capture reachable Bluetooth devices and attempt to fingerprint them.
    """
    def run(self):
        """
        Run the Sniffer main loop.
        """
        if self.adapter is not None:
            self._log.debug("Registering the signals InterfacesAdded and PropertiesChanged.")
            bus = pydbus.SystemBus()
            bus.subscribe(
                sender=SERVICE_NAME,
                iface=OBJECT_MANAGER_INTERFACE,
                signal="InterfacesAdded",
                signal_fired=self._cb_interfaces_added
            )
            bus.subscribe(
                sender=SERVICE_NAME,
                iface=PROPERTIES_INTERFACE,
                signal="PropertiesChanged",
                arg0=DEVICE_INTERFACE,
                signal_fired=self._cb_properties_changed
            )

            self._log.debug("Running the main loop.")
            if self.output_path is not None:
                GLib.timeout_add_seconds(self.backup_interval, self._cb_backup_registry)
            GLib.timeout_add_seconds(self.display_interval, self._cb_display_registry)
            loop = GLib.MainLoop()
            loop.run()
        else:
            raise ValueError("Sniffer.run can only be called in a context "
                             "(e.g. `with Sniffer(...) as s: s.run()`)")

    def _cb_interfaces_added(self, sender, obj, iface, signal, params):
        """
        Upon receiving the InterfacesAdded signal, register any new Device.
        """
        self._log.debug("Caught the signal InterfacesAddded.")
        (path, interfaces) = params
        if DEVICE_INTERFACE in interfaces:
            device = Device.create_from_dbus_dict(path, interfaces[DEVICE_INTERFACE])
            self.registry[path] = device

    def _cb_properties_changed(self, sender, obj, iface, signal, params):
        """
        Upon receiving the PropertiesChanged signal, update previously
        registered Devices.
        """
        self._log.debug("Caught the signal PropertiesChanged.")
        if DEVICE_INTERFACE in params:
            if obj in self.registry:
                self.registry[obj].update_from_dbus_dict(obj, params[1])
            else:
                self._log.warning("Received an update for a Device not in the registry.")

    def _cb_backup_registry(self):
        """
        If the backup path is set, dump the registry object to a Pickle backup.
        """
        self._log.info("Backing up the Device registry.")
        with self.output_path.open("wb") as f:
            pickle.dump(self.registry, f, protocol=pickle.HIGHEST_PROTOCOL)

        return True

    def _cb_display_registry(self):
        """
        Display the contents of the registry.
        """
        if len(self.registry) > 0:
            self._log.info("Registry Status:\n{}".format("\n\n".join(str(d) for d in self.registry.values())))

        return True

    def __init__(self, output_path=None, backup_interval=60, display_interval=50, resume=False):
        self.output_path = output_path
        self.backup_interval = backup_interval
        self.display_interval = display_interval
        self.adapter = None
        self._log = logging.getLogger("btlesniffer.Sniffer")

        if resume and self.output_path is not None and self.output_path.exists():
            self._log.info("Resuming from a previous Device registry backup.")
            with self.output_path.open("rb") as f:
                self.registry = pickle.load(f)
        else:
            self.registry = dict()

    def __enter__(self):
        self.adapter = find_adapter()
        self.adapter.StartDiscovery()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.adapter is not None:
            self.adapter.StopDiscovery()

        return False

