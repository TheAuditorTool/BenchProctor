# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest80279():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = default_blank(json_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
