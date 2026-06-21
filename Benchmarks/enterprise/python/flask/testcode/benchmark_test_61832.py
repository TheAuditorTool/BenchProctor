# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import json


def BenchmarkTest61832():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
