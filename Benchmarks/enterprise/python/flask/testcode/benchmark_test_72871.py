# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest72871():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
