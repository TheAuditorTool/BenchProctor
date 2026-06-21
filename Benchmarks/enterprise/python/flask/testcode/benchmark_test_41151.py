# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import ast


def BenchmarkTest41151():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
