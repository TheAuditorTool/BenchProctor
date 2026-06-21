# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest79147():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
