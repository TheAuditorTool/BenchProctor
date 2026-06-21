# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
import ast


def BenchmarkTest23638():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})
