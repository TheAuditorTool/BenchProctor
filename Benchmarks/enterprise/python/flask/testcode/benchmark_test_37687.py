# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest37687():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
