# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


def BenchmarkTest20068():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
