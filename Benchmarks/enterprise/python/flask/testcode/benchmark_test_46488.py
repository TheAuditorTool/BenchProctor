# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast
from app_runtime import auth_check


def BenchmarkTest46488():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
