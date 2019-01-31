#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(name='kaldi_IO',
        version='0.0.1',
        description='Glue code connecting Kaldi data and Python.',
        author='Karel Vesely',
        packages=find_packages(),
        url='https://github.com/vesis84/kaldi-io-for-python',
        install_requires=[
            'numpy>=1.15.3',
            ]
        )
