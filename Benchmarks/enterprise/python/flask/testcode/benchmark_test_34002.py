# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest34002():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
