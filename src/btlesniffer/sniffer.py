# -*- coding: utf-8 -*-

from pydbus import SystemBus


class Sniffer(object):
    def __init__(self, backup_path=None, backup_interval=60.0):
        self.backup_path = backup_path
        self.backup_interval = backup_interval
        self.bus = SystemBus()

    def run(self):
        hci0 = self.bus.get("org.bluez", "/org/bluez/hci0")
        print(hci0.Introspect())