# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


def BenchmarkTest36998():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
