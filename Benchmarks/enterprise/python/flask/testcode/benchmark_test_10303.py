# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast


def BenchmarkTest10303():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    return jsonify({'error': 'An internal error occurred'}), 500
