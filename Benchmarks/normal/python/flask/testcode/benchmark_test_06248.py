# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast


def BenchmarkTest06248():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
