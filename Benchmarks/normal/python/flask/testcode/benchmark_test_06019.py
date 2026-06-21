# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest06019():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
