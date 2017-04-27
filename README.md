# BTLE-Sniffer
This is a simple Python 3.5+ utility for monitoring Bluetooth Low Energy traffic and to register devices.

## Dependencies
As this project relies on BlueZ, it will only run on Linux
systems. The project further requires GLib2, PyGobject (commonly known as
python-gi, python-gobject or pygobject, but not packaged on PyPi) and D-Bus.

## Installing
You can now use `pip` or `setuptools` to install the package:

    $ pip install -U git+https://github.com/scipag/btle-sniffer.git

## Usage

    btlesniffer [-h] [-V] [-v] [-d] [-o OUT_PATH]
                [--backup-frequency BACKUP_FREQUENCY] [--resume]

    Scan for Bluetooth Low Energy devices and gather information about them.

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         display version information and exit
      -v, --verbose         increase the verbosity of the program
      -d, --debug           enable debugging features
      -o OUT_PATH, --out-path OUT_PATH
                            path to the device registry backup
      --backup-frequency BACKUP_FREQUENCY
                            how frequently the device registry backup should be
                            written (in seconds)
      --resume              resume from a previous device registry backup (must
                            specify the `-o` option)
