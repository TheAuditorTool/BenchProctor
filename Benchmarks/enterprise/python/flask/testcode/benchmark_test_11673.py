# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def ensure_str(value):
    return str(value)

def BenchmarkTest11673():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ensure_str(json_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
