# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest32811():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})
