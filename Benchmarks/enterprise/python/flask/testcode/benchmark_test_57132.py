# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
from types import SimpleNamespace


def BenchmarkTest57132():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
