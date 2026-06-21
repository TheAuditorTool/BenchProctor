# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast


def BenchmarkTest18640():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
