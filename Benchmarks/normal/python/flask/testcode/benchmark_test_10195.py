# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import ast


def BenchmarkTest10195():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
