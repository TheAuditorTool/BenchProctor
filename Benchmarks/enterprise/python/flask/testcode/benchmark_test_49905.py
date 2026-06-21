# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast


def BenchmarkTest49905():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
