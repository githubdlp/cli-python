#!/usr/bin/env python

""" ODCS CLI : setup.py"""

import os
from setuptools import setup, find_packages

CURDIR = os.path.abspath(os.path.dirname(__file__))
NAME = "odcscli"
DESCRIPTION = "ODCS Command Line Interface"
INSTALL_REQUIRES = ["requests>=2.7.0,<=2.8.1", "keyring>=5.4,<=5.6", "colorama==0.3.3", "PyYAML==3.11"]
KEYWORDS = ["odcs", "odcscli"]
PACKAGES = ["odcscliscript"]
CLASSIFIERS = [
    "Natural Language :: English",
    "License :: OSI Approved :: Common Public License",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5"
]
SCRIPTS = ["odcs", "odcs.cmd"]

setup_options = dict(
    name=NAME,
    description=DESCRIPTION,
    long_description=open(CURDIR+"/README.rst").read(),
    version='0.1',
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    scripts=SCRIPTS,
)

setup(**setup_options)
