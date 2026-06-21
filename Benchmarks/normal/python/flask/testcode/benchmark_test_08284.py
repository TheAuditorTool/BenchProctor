# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import ast


def BenchmarkTest08284():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
