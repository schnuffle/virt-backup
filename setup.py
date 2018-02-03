#!/usr/bin/env python3

"""
Automatic backups for libvirt
See:
    https://github.com/Anthony25/virt-backup
"""

from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
    name="virt-backup",
    version="0.1.5",

    description="Automatic backups for libvirt",

    url="https://github.com/Anthony25/virt-backup",
    author="Anthony25 <Anthony Ruhier>",
    author_email="anthony.ruhier@gmail.com",

    license="Simplified BSD",

    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
    ],

    keywords="libvirt",
    packages=["virt_backup", "virt_backup.groups", "virt_backup.backups"],
    install_requires=[
        "appdirs", "argparse", "arrow", "defusedxml", "libvirt-python", "lxml",
        "tqdm", "PyYAML", "lz4tools"
    ],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', 'pytest-cov', "pytest-mock"],
    entry_points={
        'console_scripts': [
            'virt-backup = virt_backup.__main__:parse_args',
        ],
    }
)
