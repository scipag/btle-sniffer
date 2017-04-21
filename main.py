#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scan for Bluetooth Low Energy packets and attempt to identify them.
"""

import os
import sys
import argparse
import logging
import pathlib

from hci_parser import HciParser


REQUIRE_PLATFORM = "linux"
REQUIRE_UID = 0


def main() -> None:
    if sys.platform != REQUIRE_PLATFORM:
        raise RuntimeError("You must run this programme on Linux.")

    if os.geteuid() != REQUIRE_UID:
        raise PermissionError("You must be root to run this programme.")

    parser = argparse.ArgumentParser(
        prog="btle-sniffer",
        description="Scan for Bluetooth Low Energy devices and gather information about them."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="increase the verbosity of the program"
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="enable debugging features"
    )
    parser.add_argument(
        "-o", "--out-file",
        type=str,
        help="path to the dump file"
    )
    parser.add_argument(
        "--backup-frequency",
        type=float,
        default=60.0,
        help="how frequently the backup file should be written (in seconds)"
    )
    args = parser.parse_args()

    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2 or args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)

    if args.out_file is not None:
        backup_path = pathlib.Path(args.out_file)
    else:
        backup_path = None

    with HciParser(backup_path, args.backup_frequency) as parser:
        parser.run()


if __name__ == "__main__":
    main()
