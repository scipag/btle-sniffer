# BTLE-Sniffer
This is a simple Python 3.5+ utility for monitoring Bluetooth Low Energy traffic and to register devices.

## Dependencies
As this project relies on BlueZ and libbluetooth, it will only run on Linux
systems. Currently, there are no other dependencies.

## Installing
You can now use `pip` or `setuptools` to install the package:

    $ pip install -U git+https://github.com/scipag/btle-sniffer.git

## Usage

    btlesniffer [-h] [-V] [-v] [-d] [-o OUT_FILE]
                [--backup-frequency BACKUP_FREQUENCY]

    Scan for Bluetooth Low Energy devices and gather information about them.

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         display version information and exit
      -v, --verbose         increase the verbosity of the program
      -d, --debug           enable debugging features
      -o OUT_FILE, --out-file OUT_FILE
                            path to the dump file
      --backup-frequency BACKUP_FREQUENCY
                            how frequently the backup file should be written (in
                            seconds)

