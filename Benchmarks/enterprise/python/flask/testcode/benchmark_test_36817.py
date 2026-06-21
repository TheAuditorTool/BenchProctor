# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast


def BenchmarkTest36817():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
