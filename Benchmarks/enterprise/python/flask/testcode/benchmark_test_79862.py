# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
import ast


def BenchmarkTest79862():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if os.environ.get("APP_ENV", "production") != "test":
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return jsonify({"result": "success"})
