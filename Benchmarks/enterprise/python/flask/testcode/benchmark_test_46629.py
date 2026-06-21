# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast


def BenchmarkTest46629():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
