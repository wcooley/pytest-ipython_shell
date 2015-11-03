# -*- coding: utf-8 -*-

"""py.test plugin to start an IPython interpreter."""

from __future__ import print_function, unicode_literals

import logging

import pytest

log = logging.getLogger(__name__)  # pylint: disable=invalid-name


def pytest_namespace():
    return {'ipython_shell': pytestIPython().get_ipython_shell}


# Cargo-culted from _pytest/pdb.py
def pytest_configure(config):
    old = (pytestIPython._pluginmanager,)
    def fin():
        pytestIPython._pluginmanager, = old
        pytestIPython._config = None
    pytestIPython._pluginmanager = config.pluginmanager
    pytestIPython._config = config
    config._cleanup.append(fin)


class pytestIPython:
    _pluginmanager = None
    _config = None

    def get_ipython_shell(self, **kwargs):
        import _pytest.config
        import IPython

        capman = None
        tw = _pytest.config.create_terminal_writer(self._config)
        if self._pluginmanager is not None:
            capman = self._pluginmanager.getplugin("capturemanager")
            if capman:
                capman.suspendcapture(in_=True)
            tw.line()
        tw.sep(">", "IPython (IO-capturing turned off)")

        from IPython.terminal.embed import InteractiveShellEmbed
        return InteractiveShellEmbed()
