# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest01458(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
