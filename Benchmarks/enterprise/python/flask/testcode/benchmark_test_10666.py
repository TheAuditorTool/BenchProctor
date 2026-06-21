# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from types import SimpleNamespace


def BenchmarkTest10666():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
