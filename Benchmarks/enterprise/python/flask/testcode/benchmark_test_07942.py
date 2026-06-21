# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest07942():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
