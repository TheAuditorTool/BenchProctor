# SPDX-License-Identifier: Apache-2.0
from flask import request
from types import SimpleNamespace


def BenchmarkTest35750():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
