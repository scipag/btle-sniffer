# -*- coding: utf-8 -*-

import os
import ctypes
import ctypes.util
import errno


class BluezError(Exception):
    def __init__(self, function):
        err_num = ctypes.get_errno()
        message = "In {}: {} ({}).".format(function, os.strerror(err_num), errno.errorcode[err_num])
        super(BluezError, self).__init__(message)


btlib = ctypes.util.find_library("bluetooth")
if btlib is None:
    raise ImportError("Cannot find the Bluetooth library.")

bluez = ctypes.CDLL(btlib, use_errno=True)


def hci_get_route():
    dev_id = bluez.hci_get_route(None)
    if dev_id < 0:
        raise BluezError("hci_get_route")

    return dev_id


def hci_le_set_scan_parameters(sock, scan_type, scan_interval, scan_window, address_type, filter_policy, timeout):
    err = bluez.hci_le_set_scan_parameters(
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


def hci_le_set_scan_enable(sock, enable, filter_duplicates, timeout):
    err = bluez.hci_le_set_scan_enable(
        sock.fileno(),
        enable,
        filter_duplicates,
        timeout
    )
    if err < 0:
        raise BluezError("hci_le_set_scan_enable")