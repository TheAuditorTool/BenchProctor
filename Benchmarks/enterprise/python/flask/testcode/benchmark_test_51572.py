# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest51572():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
