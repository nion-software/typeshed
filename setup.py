# -*- coding: utf-8 -*-

import setuptools
import os

setuptools.setup(
    name="nion.typeshed",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['numpy'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha"
    ],
    include_package_data=True
)
