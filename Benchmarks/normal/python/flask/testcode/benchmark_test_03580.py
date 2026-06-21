# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest03580():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    return jsonify({'error': 'An internal error occurred'}), 500
