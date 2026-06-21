# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest63278():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
