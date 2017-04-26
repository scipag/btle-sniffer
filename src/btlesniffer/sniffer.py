# -*- coding: utf-8 -*-

"""
Provide a class that uses the D-Bus API of BlueZ to capture nearby Bluetooth
devices.
"""

import time
import json

import pydbus
import gi.repository

from .util import SERVICE_NAME, DEVICE_INTERFACE, OBJECT_MANAGER_INTERFACE, \
    PROPERTIES_INTERFACE, find_adapter


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
                sender=SERVICE_NAME,
                iface=OBJECT_MANAGER_INTERFACE,
                signal="InterfacesAdded",
                signal_fired=self._cb_interface_added
            )
            bus.subscribe(
                sender=SERVICE_NAME,
                iface=PROPERTIES_INTERFACE,
                signal="PropertiesChanged",
                arg0=DEVICE_INTERFACE,
                signal_fired=self._cb_properties_updated
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
        if DEVICE_INTERFACE in interfaces:
            self.registry.append(interfaces[DEVICE_INTERFACE])
            # print(interfaces[DEVICE_INTERFACE])

            new_time = time.monotonic()
            if (new_time - self.current_time) >= self.backup_interval:
                self.current_time = new_time
                self._backup_registry()

    def _cb_properties_updated(self, sender, object, iface, signal, params):
        print(params)

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

