# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest12755():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
