# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests
from types import SimpleNamespace


def BenchmarkTest23613():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
