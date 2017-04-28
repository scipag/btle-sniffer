#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import setuptools
import versioneer

if __name__ == "__main__":
    long_description_path = pathlib.Path("README.md")
    setuptools.setup(
        name="btlesniffer",
        author="Eleanore C. Young",
        author_email="youngelliecaitlin@gmail.com",
        description="Scan for and attempt to fingerprint Bluetooth LE devices.",
        long_description=long_description_path.read_text(),
        keywords="bluetooth, bluetooth-low-energy, sniffer, sniffing, security,"
                 "security-audit, security-scanner, security-protocol,"
                 "security-vulnerability, security-hardening, wireless,"
                 "wireless-network, wireless-communication",
        license="MIT",
        url="https://github.com/scipag/btle-sniffer.git",
        classifiers=(
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Information Technology",
            "License :: OSI Approved :: MIT License",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6"
        ),
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        platforms=("linux",),
        install_requires=(
            "pydbus",
        ),
        entry_points={
            "console_scripts": ("btlesniffer = btlesniffer.main:main",)
        },
        packages=setuptools.find_packages(where="src"),
        package_dir={"": "src"}
    )
