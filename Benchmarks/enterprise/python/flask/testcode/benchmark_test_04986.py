# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest04986():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
