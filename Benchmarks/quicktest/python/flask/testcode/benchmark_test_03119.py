# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import ast


def BenchmarkTest03119():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    json.loads(data)
    return jsonify({"result": "success"})
