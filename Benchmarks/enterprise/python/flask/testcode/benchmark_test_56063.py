# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest56063():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(json_value)}, verify=True)
    return jsonify({"result": "success"})
