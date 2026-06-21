# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast


def BenchmarkTest23798():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
