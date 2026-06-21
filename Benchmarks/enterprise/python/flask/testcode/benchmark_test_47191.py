# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest47191():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
