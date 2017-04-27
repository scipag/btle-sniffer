# -*- coding: utf-8 -*-

"""
Provide a class that uses the D-Bus API of BlueZ to capture nearby Bluetooth
devices.
"""

import logging
import pickle

import pydbus
from gi.repository import GLib

from .util import SERVICE_NAME, DEVICE_INTERFACE, OBJECT_MANAGER_INTERFACE, \
    PROPERTIES_INTERFACE, find_adapter


class Device(object):
    @classmethod
    def create_from_dbus_dict(cls, data):
        return cls(
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

    def update_from_dbus_dict(self, data):
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
            pass
        if "ServiceData" in data:
            pass

    def __init__(self, address, paired, connected, services_resolved,
                 name=None, device_class=None, appearance=None,
                 uuids=None, rssi=None, tx_power=None, manufacturer_data=None,
                 service_data=None):
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
        self.manufacturer_data = manufacturer_data
        self.service_data = service_data

    def __repr__(self):
        return "{}{}".format(self.__class__.__name__, (
            self.addresses, self.paired, self.connected, self.services_resolved,
            self.name, self.device_class, self.appearance, self.uuids,
            self.rssis, self.tx_power, self.manufacturer_data, self.service_data
        ))

    def __str__(self):
        return "<{}>".format(self.addresses)


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
            GLib.timeout_add_seconds(self.backup_interval, self._cb_backup_degistry)
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
            self.registry[path] = Device.create_from_dbus_dict(interfaces[DEVICE_INTERFACE])

    def _cb_properties_changed(self, sender, obj, iface, signal, params):
        """
        Upon receiving the PropertiesChanged signal, update previously
        registered Devices.
        """
        self._log.debug("Caught the signal PropertiesChanged.")
        if DEVICE_INTERFACE in params:
            if obj in self.registry:
                self.registry[obj].update_from_dbus_dict(params[1])
            else:
                self._log.warning("Received an update for a Device not in the registry.")

    def _cb_backup_degistry(self):
        """
        If the backup path is set, dump the registry object to a Pickle backup.
        """
        if self.output_path is not None:
            self._log.info("Backing up the Device registry.")
            with self.output_path.open("wb") as f:
                pickle.dump(self.registry, f, protocol=pickle.HIGHEST_PROTOCOL)

        return True

    def __init__(self, output_path=None, backup_interval=60.0, resume=False):
        self.output_path = output_path
        self.backup_interval = backup_interval
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

