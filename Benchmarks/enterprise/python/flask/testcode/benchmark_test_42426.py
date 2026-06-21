# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest42426():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
