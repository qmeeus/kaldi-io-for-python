#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019  Oplatai.com (author: Ondrej Platek)
# Licensed under the Apache License, Version 2.0 (the "License")

from setuptools import setup, find_packages
setup(name='kaldi_io',
        version='0.0.1',
        description='Glue code connecting Kaldi data and Python.',
        author='Karel Vesely',
        packages=find_packages(),
        url='https://github.com/vesis84/kaldi-io-for-python',
        install_requires=[
            'numpy>=1.15.3',
            ]
        )
