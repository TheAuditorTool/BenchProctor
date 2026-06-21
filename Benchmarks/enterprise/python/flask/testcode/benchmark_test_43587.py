# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import ast
from app_runtime import auth_check


def BenchmarkTest43587(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
