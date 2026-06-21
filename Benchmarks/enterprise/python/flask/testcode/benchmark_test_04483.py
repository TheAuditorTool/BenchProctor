# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib
from types import SimpleNamespace


def BenchmarkTest04483():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
