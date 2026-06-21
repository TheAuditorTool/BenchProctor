# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request, jsonify


def BenchmarkTest76922():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
