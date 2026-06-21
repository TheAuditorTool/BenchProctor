# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import ast


def BenchmarkTest69210():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    session['user'] = str(data)
    return jsonify({"result": "success"})
