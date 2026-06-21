# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import ast
from app_runtime import auth_check


def BenchmarkTest38368():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
