# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest09656():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
