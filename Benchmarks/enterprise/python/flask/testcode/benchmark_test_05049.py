# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
from types import SimpleNamespace


def BenchmarkTest05049():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
