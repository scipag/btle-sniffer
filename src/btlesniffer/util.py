# -*- coding: utf-8 -*-

"""
Provide various utility functions for interacting with D-Bus and BlueZ.
With only minor changes, this code is based on the bluezutils.py test script
at https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/test/bluezutils.py
"""

import pydbus

SERVICE_NAME = "org.bluez"
ADAPTER_INTERFACE = "{}.Adapter1".format(SERVICE_NAME)
DEVICE_INTERFACE = "{}.Device1".format(SERVICE_NAME)
GATT_SERVICE_INTERFACE = "{}.GattService1".format(SERVICE_NAME)
GATT_CHARACTERISTIC_INTERFACE = "{}.GattCharacteristic1".format(SERVICE_NAME)
GATT_DESCRIPTOR_INTERFACE = "{}.GattDescriptor1".format(SERVICE_NAME)
OBJECT_MANAGER_INTERFACE = "org.freedesktop.DBus.ObjectManager"
PROPERTIES_INTERFACE = "org.freedesktop.DBus.Properties"


class BlueZDBusException(Exception):
    pass


def get_managed_objects():
    """
    Use the D-Bus ObjectManager interface to determine all managed objects
    of the BlueZ service.
    """
    bus = pydbus.SystemBus()
    manager = bus.get(SERVICE_NAME, "/")[OBJECT_MANAGER_INTERFACE]
    return manager.GetManagedObjects()


def find_adapter_in_objects(objects, pattern=None):
    """
    Given a dictionary of objects, find either the first Adapter interface
    or the one defined by the specified string pattern.
    """
    bus = pydbus.SystemBus()
    for path, ifaces in objects.items():
        adapter = ifaces.get(ADAPTER_INTERFACE)
        if adapter is not None:
            if pattern is None or pattern == adapter.Address or path.endswith(pattern):
                return bus.get(SERVICE_NAME, path)[ADAPTER_INTERFACE]
    else:
        raise BlueZDBusException("Bluetooth adapter not found.")


def find_device_in_objects(objects, device_address, adapter_pattern=None):
    """
    Given a dictionary of objects, find the Device interface that
    corresponds to the given address and the related adapter pattern.
    """
    bus = pydbus.SystemBus()
    path_prefix = ""
    if adapter_pattern is not None:
        adapter = find_adapter_in_objects(objects, adapter_pattern)
        path_prefix = adapter._path

    for path, ifaces in objects.items():
        device = ifaces.get(DEVICE_INTERFACE)
        if device is not None:
            if device.Address == device_address and path.startswith(path_prefix):
                return bus.get(SERVICE_NAME, path)[DEVICE_INTERFACE]
    else:
        raise BlueZDBusException(
            "Bluetooth device '{}' not found.".format(device_address)
        )


def find_adapter(pattern=None):
    """
    Find either the first Adapter interface or the one defined by the
    specified string pattern.
    """
    return find_adapter_in_objects(get_managed_objects(), pattern)


def find_device(device_address, adapter_pattern=None):
    """
    Find the Device interface specified by the given address and the
    corresponding adapter pattern.
    """
    return find_device_in_objects(
        get_managed_objects(), device_address, adapter_pattern
    )


def get_known_devices():
    """
    Using the DBus ObjectManager, yield all known Devices.
    """
    bus = pydbus.SystemBus()
    manager = bus.get(SERVICE_NAME, "/")[OBJECT_MANAGER_INTERFACE]
    objs = manager.GetManagedObjects()
    for path, ifaces in objs.items():
        if DEVICE_INTERFACE in ifaces.keys():
            yield (path, ifaces[DEVICE_INTERFACE])


def get_known_services():
    """
    Using the DBus ObjectManager, yield all known GATT services.
    """
    bus = pydbus.SystemBus()
    manager = bus.get(SERVICE_NAME, "/")[OBJECT_MANAGER_INTERFACE]
    objs = manager.GetManagedObjects()
    for path, ifaces in objs.items():
        if GATT_SERVICE_INTERFACE in ifaces.keys():
            yield (path, ifaces[GATT_SERVICE_INTERFACE])
