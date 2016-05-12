# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="nion.typeshed",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['niondata', 'nionutils', 'numpy'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
