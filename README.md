# BTLE-Sniffer
This is a simple Python 3.5+ utility for monitoring Bluetooth Low Energy traffic and to register devices.

In the short term, this will be converted to a proper Python distutils package, but for now, the scripts are as is.

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

