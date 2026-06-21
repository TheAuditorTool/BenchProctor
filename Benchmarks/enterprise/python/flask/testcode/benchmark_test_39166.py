# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import requests


def BenchmarkTest39166():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = data[:64]
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return jsonify({"result": "success"})
