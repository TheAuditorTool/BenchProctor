# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast


def BenchmarkTest34589():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
