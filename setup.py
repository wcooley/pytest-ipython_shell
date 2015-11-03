#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup project."""

import os
import codecs
from setuptools import setup


def _read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-ipython_shell',
    version='0.1.0',
    author='Wil Cooley',
    author_email='wcooley@nakedape.cc',
    maintainer='Wil Cooley',
    maintainer_email='wcooley@nakedape.cc',
    license='MIT',
    url='https://github.com/wcooley/pytest-ipython_shell',
    description='A py.test plugin to start an IPython interpreter within a test.',
    long_description=_read('README.rst'),
    packages=['pytest_ipython_shell'],
    install_requires=['pytest>=2.8.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    keywords='pytest py.test ipython plugin',
    entry_points={
        'pytest11': [
            'ipython_shell = pytest_ipython_shell.plugin',
        ],
    },
)
