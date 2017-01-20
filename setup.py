# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="nion.typeshed",
    version="0.0.1",
    url="https://github.com/nion-software/typeshed",
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['niondata', 'nionutils', 'numpy'],
    license='Apache 2.0',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
    ],
    include_package_data=True
)
