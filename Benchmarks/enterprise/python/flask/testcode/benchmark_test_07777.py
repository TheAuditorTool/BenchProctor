# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import ast


def BenchmarkTest07777():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
