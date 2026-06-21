# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast


def BenchmarkTest01539():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if os.environ.get("APP_ENV", "production") != "test":
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
