# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest10872():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})
