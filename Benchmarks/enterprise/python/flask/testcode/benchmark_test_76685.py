# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request, jsonify


def BenchmarkTest76685():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
