# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest47251():
    secret_value = 'app_display_name'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
