# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from types import SimpleNamespace


def BenchmarkTest71664():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
