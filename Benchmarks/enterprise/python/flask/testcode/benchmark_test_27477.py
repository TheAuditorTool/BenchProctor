# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from types import SimpleNamespace


def BenchmarkTest27477():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
