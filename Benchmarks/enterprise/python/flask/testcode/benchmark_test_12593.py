# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast
from app_runtime import auth_check


def BenchmarkTest12593():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
