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
from .device import Device


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
        Upon receiving the InterfacesAdded signal, register any new device.
        """
        self._log.debug("Caught the signal InterfacesAddded.")
        (path, interfaces) = params
        if DEVICE_INTERFACE in interfaces:
            self._register_device(Device.create_from_dbus_dict(path, interfaces[DEVICE_INTERFACE]))

    def _cb_properties_changed(self, sender, obj, iface, signal, params):
        """
        Upon receiving the PropertiesChanged signal, update previously
        registered devices.
        """
        self._log.debug("Caught the signal PropertiesChanged.")
        if DEVICE_INTERFACE in params:
            device = self._find_device_by_path(obj)
            if device is not None:
                device.update_from_dbus_dict(obj, params[1])
            else:
                self._log.warning("Received an update for a device not in the registry.")

    def _cb_backup_registry(self):
        """
        If the backup path is set, dump the registry object to a Pickle backup.
        """
        self._log.info("Backing up the device registry.")
        with self.output_path.open("wb") as f:
            pickle.dump(self.registry, f, protocol=pickle.HIGHEST_PROTOCOL)

        return True

    def _cb_display_registry(self):
        """
        Display the contents of the registry.
        """
        if len(self.registry) > 0:
            self._log.info("Registry Status:\n{}".format("\n\n".join(str(d) for d in self.registry)))

        return True

    def _register_device(self, device):
        for d in self.registry:
            if device == d:
                self._log.debug("Updating an existing device.")
                d.update_from_device(device)
                return
        else:
            self._log.debug("Adding a new device.")
            self.registry.append(device)

    def _find_device_by_path(self, path):
        for d in self.registry:
            if path in d.paths:
                return d

    def __init__(self, output_path=None, backup_interval=60, display_interval=30, resume=False):
        self.output_path = output_path
        self.backup_interval = backup_interval
        self.display_interval = display_interval
        self.adapter = None
        self._log = logging.getLogger("btlesniffer.Sniffer")

        if resume and self.output_path is not None and self.output_path.exists():
            self._log.info("Resuming from a previous device registry backup.")
            with self.output_path.open("rb") as f:
                self.registry = pickle.load(f)
        else:
            self.registry = list()

    def __enter__(self):
        self._log.debug("Choosing the first available Bluetooth adapter and "
                        "starting device discovery.")
        self.adapter = find_adapter()
        self.adapter.StartDiscovery()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.adapter is not None:
            self._log.debug("Stopping device discovery.")
            self.adapter.StopDiscovery()

        return False

