# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from types import SimpleNamespace


def BenchmarkTest75196():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
