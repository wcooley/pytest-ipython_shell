"""py.test config hook."""

from __future__ import print_function, unicode_literals

import pytest


def pytest_addoption(parser):
    """Add option to enable tests requiring interaction."""
    parser.addoption('--interactive-test', '--interactive-tests',
            action='store_true', default=False, help='Enable interactive tests',
            dest='interactive-test')


pytest_plugins = 'pytester'
