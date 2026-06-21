# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import ast


def BenchmarkTest02587():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
