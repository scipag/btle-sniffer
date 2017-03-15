# -*- coding: utf-8 -*-

"""
Provides a thin wrapper around the Linux Bluetooth library, BlueZ.
"""

import os
import ctypes
import ctypes.util
import errno
import socket

import hci_constants

BLUETOOTH_LIBRARY_NAME = ctypes.util.find_library("bluetooth")
if BLUETOOTH_LIBRARY_NAME is None:
    raise ImportError("Cannot find the Bluetooth library.")

BLUEZ = ctypes.CDLL(BLUETOOTH_LIBRARY_NAME, use_errno=True)


class BluezError(Exception):
    """
    The BlueZ error class generates the error message from the causing function name name and ERRNO.
    """
    def __init__(self, function_name):
        err_num = ctypes.get_errno()
        message = "In {}: {} ({}).".format(
            function_name, os.strerror(err_num), errno.errorcode[err_num]
        )
        super(BluezError, self).__init__(message)


def hci_get_route() -> int:
    """
    Return the first Bluetooth device ID.
    """
    dev_id = BLUEZ.hci_get_route(None)
    if dev_id < 0:
        raise BluezError("hci_get_route")

    return dev_id


def hci_le_set_scan_parameters(
        sock: socket.socket,
        scan_type: hci_constants.ScanType,
        scan_interval: int,
        scan_window: int,
        address_type: hci_constants.AddressType,
        filter_policy: hci_constants.FilterPolicy,
        timeout: int
    ) -> None:
    """
    Set LE scanning parameters.
    """
    err = BLUEZ.hci_le_set_scan_parameters(
        sock.fileno(),
        scan_type.value,
        scan_interval,
        scan_window,
        address_type.value,
        filter_policy.value,
        timeout
    )
    if err < 0:
        raise BluezError("hci_le_set_scan_parameters")


def hci_le_set_scan_enable(
        sock: socket.socket,
        enable: bool,
        filter_duplicates: bool,
        timeout: int
    ) -> None:
    """
    Enable or disable LE scanning.
    """
    err = BLUEZ.hci_le_set_scan_enable(
        sock.fileno(),
        enable,
        filter_duplicates,
        timeout
    )
    if err < 0:
        raise BluezError("hci_le_set_scan_enable")
