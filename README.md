# BTLE-Sniffer
This is a simple Python 3.5+ utility for monitoring Bluetooth Low Energy 
traffic and to register devices. Thanks to D-Bus, it does not require
elevated privileges to be run!

## Dependencies
As this project relies on BlueZ, it will only run on Linux
systems. The project further requires GLib2, PyGobject (commonly known as
python-gi, python-gobject or pygobject, but not packaged on PyPi) and D-Bus.

## Installing
You can now use `pip` or `setuptools` to install the package:

    $ pip install -U git+https://github.com/scipag/btle-sniffer.git

## Usage

    usage: btlesniffer [-h] [-V] [-v] [-d] [-o OUT_PATH] [-i BACKUP_INTERVAL] [-r]
                       [-c] [--threshold-rssi THRESHOLD_RSSI]
                       [--connection-polling-interval CONNECTION_POLLING_INTERVAL]

    Scan for Bluetooth Low Energy devices and gather information about them. This
    program will only run on Linux systems.

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         display version information and exit
      -v, --verbose         increase the verbosity of the program
      -d, --debug           enable debugging features
      -o OUT_PATH, --out-path OUT_PATH
                            path to the device registry backup
      -i BACKUP_INTERVAL, --backup-interval BACKUP_INTERVAL
                            how frequently the device registry backup should be
                            written (in seconds, default 5 s). If set to zero, the
                            backup will be written with every device update.
      -r, --resume          resume from a previous device registry backup (must
                            specify the `-o` option)
      -c, --connect         attempt to connect to all discovered Bluetooth devices
      --threshold-rssi THRESHOLD_RSSI
                            the lower bound received signal strength (RSSI) at
                            which to attempt to connect to devices (in dBa,
                            default -80 dBa).
      --connection-polling-interval CONNECTION_POLLING_INTERVAL
                            how frequently the sniffer shall go through the device
                            registry and attempt to establish connections (in
                            seconds, default 5 s).

