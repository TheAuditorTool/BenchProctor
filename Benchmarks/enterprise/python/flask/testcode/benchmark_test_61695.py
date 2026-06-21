# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest61695():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
