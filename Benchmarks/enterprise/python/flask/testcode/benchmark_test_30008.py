# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast


def BenchmarkTest30008():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    if os.environ.get("APP_ENV", "production") != "test":
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
