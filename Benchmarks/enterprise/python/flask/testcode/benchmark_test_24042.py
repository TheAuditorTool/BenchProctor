# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast
from app_runtime import auth_check


def BenchmarkTest24042():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
