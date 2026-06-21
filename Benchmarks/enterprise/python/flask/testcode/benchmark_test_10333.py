# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest10333():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(json_value)}, verify=False)
    return jsonify({"result": "success"})
