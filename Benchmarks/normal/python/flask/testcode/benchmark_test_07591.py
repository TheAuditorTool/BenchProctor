# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest07591():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
