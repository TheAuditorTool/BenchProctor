# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
from types import SimpleNamespace


def BenchmarkTest00775():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    def _primary():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
