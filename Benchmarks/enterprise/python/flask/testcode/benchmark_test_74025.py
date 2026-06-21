# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest74025():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
