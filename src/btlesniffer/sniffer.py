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
    PROPERTIES_INTERFACE, find_adapter, GATT_SERVICE_INTERFACE, \
    GATT_CHARACTERISTIC_INTERFACE, GATT_DESCRIPTOR_INTERFACE, get_known_devices
from .device import GATTService, Device, print_device


class Sniffer(object):
    """
    Capture reachable Bluetooth devices and attempt to fingerprint them.
    """
    def run(self):
        """
        Run the Sniffer main loop.
        """
        if self.adapter is not None:
            self._log.debug("Clearing the BlueZ device registry.")
            for path, _ in get_known_devices():
                self.adapter.RemoveDevice(path)

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
                iface=OBJECT_MANAGER_INTERFACE,
                signal="InterfacesRemoved",
                signal_fired=self._cb_interfaces_removed
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
        self._log.debug("Added: {}".format(params))
        (path, interfaces) = params
        if DEVICE_INTERFACE in interfaces:
            self._register_device(Device.create_from_dbus_dict(path, interfaces[DEVICE_INTERFACE]))
        if GATT_SERVICE_INTERFACE in interfaces:
            self._register_service(path, interfaces[GATT_SERVICE_INTERFACE])

    def _cb_interfaces_removed(self, sender, obj, iface, signal, params):
        """
        Upon receiving the InterfacesRemoved signal, note the loss of a device.
        """
        self._log.debug("Caught the signal InterfacesRemoved.")
        self._log.debug("Removed: {}".format(params))
        (path, ifaces) = params
        device = self._find_device_by_path(path)
        if device is not None:
            device.active = False

    def _cb_properties_changed(self, sender, obj, iface, signal, params):
        """
        Upon receiving the PropertiesChanged signal, update previously
        registered devices.
        """
        if DEVICE_INTERFACE in params:
            device = self._find_device_by_path(obj)
            if device is not None:
                device.update_from_dbus_dict(obj, params[1])
            else:
                self._log.debug("Received PropertiesChanged for an "
                                "unknown device.")

    def _cb_backup_registry(self):
        """
        If the backup path is set, dump the registry object to a Pickle backup.
        """
        self._log.info("Backing up the device registry.")
        with self.output_path.open("wb") as f:
            pickle.dump(self.registry, f, protocol=pickle.HIGHEST_PROTOCOL)

        return True

    def _register_device(self, device):
        d = self._find_device(device)
        if d is not None:
            d.update_from_device(device)
            if self.attempt_connection:
                self._connect(d)
            print_device(d, "Update")
        else:
            self.registry.append(device)
            if self.attempt_connection:
                self._connect(device)
            print_device(device, "New")

    def _register_service(self, path, service):
        device_path = service["Device"]
        device = self._find_device_by_path(device_path)
        if device is not None:
            device[path] = GATTService(service["UUID"], service["Primary"])
            print_device(device, "Update")
        else:
            self._log.debug("Received a service for an unknown device.")

    def _connect(self, device):
        if not device.connected:
            device.connected = True
            print_device(device, "Connecting")
            def cb_connect():
                bus = pydbus.SystemBus()
                proxy = bus.get(SERVICE_NAME, device.path)
                try:
                    proxy.Connect()
                except KeyError:
                    self._log.exception("Something is wrong with pydbus.")
                except GLib.Error:
                    self._log.debug("Connect() failed:", exc_info=True)
            GLib.idle_add(cb_connect)

    def _find_device(self, device):
        for d in self.registry:
            if device == d:
                return d

    def _find_device_by_path(self, path):
        for d in self.registry:
            if path == d.path:
                return d

    def __init__(self, output_path=None, backup_interval=5, resume=False, attempt_connection=False):
        self.output_path = output_path
        self.backup_interval = backup_interval
        self.attempt_connection = attempt_connection
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
        self._log.debug("The discovery filter is set to Bluetooth LE only.")
        self.adapter.SetDiscoveryFilter({"Transport": pydbus.Variant("s", "le")})
        self.adapter.StartDiscovery()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.adapter is not None:
            self._log.debug("Stopping device discovery.")
            self.adapter.StopDiscovery()

        return False

