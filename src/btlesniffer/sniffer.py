# -*- coding: utf-8 -*-

"""
Provide a class that uses the D-Bus API of BlueZ to capture nearby Bluetooth
devices.
"""

import time
import json

import pydbus
import gi.repository

from .util import find_adapter


class Device(object):
    def __init__(self, address, paired, connected, legacy_pairing,
                 services_resolved, name=None, icon=None, device_class=None,
                 appearance=None, uuids=None, rssi=None, tx_power=None,
                 manufacturer_data=None, service_data=None,
                 advertising_flags=None):
        self.address = address
        self.name = name
        self.icon = icon
        self.device_class = device_class
        self.appearance = appearance
        self.uuids = uuids
        self.paired = paired
        self.connected = connected
        self.legacy_pairing = legacy_pairing
        self.rssi = rssi
        self.tx_power = tx_power
        self.manufacturer_data = manufacturer_data
        self.service_data = service_data
        self.services_resolved = services_resolved
        self.advertising_flags = advertising_flags

    def __repr__(self):
        return "{}{!r}".format(
            self.__class__.__name__, (self.address, self.name, self.icon,
            self.device_class, self.appearance, self.uuids, self.paired,
            self.connected, self.legacy_pairing, self.rssi, self.tx_power,
            self.manufacturer_data, self.service_data, self.services_resolved,
            self.advertising_flags)
        )

    def __str__(self):
        if self.name is None:
            name = "Unknown"
        else:
            name = self.name
        return "<{}, {}>".format(name, self.address)


class Sniffer(object):
    """
    Capture reachable Bluetooth devices and attempt to fingerprint them.
    """
    def run(self):
        """
        Run the Sniffer main loop.
        """
        if self.adapter is not None:
            bus = pydbus.SystemBus()
            bus.subscribe(
                sender="org.bluez",
                iface="org.freedesktop.DBus.ObjectManager",
                signal="InterfacesAdded",
                signal_fired=self._cb_interface_added
            )
            loop = gi.repository.GLib.MainLoop()

            self.current_time = time.monotonic()
            loop.run()
        else:
            raise ValueError("Sniffer.run can only be called in a context "
                             "(e.g. `with Sniffer(...) as s: s.run()`)")

    def _backup_registry(self):
        """
        If the backup path is set, dump the registry object to a Pickle backup.
        """
        if self.backup_path is not None:
            with self.backup_path.open("w") as f:
                json.dump(self.registry, f)

    def _cb_interface_added(self, sender, object, iface, signal, params):
        (path, interfaces) = params
        if "org.bluez.Device1" in interfaces:
            self.registry.append(interfaces["org.bluez.Device1"])
            print(interfaces["org.bluez.Device1"])

            new_time = time.monotonic()
            if (new_time - self.current_time) >= self.backup_interval:
                self.current_time = new_time
                self._backup_registry()

    def __init__(self, backup_path=None, backup_interval=60.0):
        self.backup_path = backup_path
        self.backup_interval = backup_interval
        self.adapter = None
        self.registry = list()
        self.current_time = None

    def __enter__(self):
        self.adapter = find_adapter()
        self.adapter.StartDiscovery()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.adapter is not None:
            self.adapter.StopDiscovery()

        return False

