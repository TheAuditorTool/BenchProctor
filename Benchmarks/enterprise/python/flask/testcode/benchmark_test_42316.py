# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
import ast


def BenchmarkTest42316():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
