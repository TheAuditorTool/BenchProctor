# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest37436():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})
