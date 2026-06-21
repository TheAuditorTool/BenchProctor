# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import ast
from app_runtime import auth_check


def BenchmarkTest59305():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    auth_check('user', data)
    return jsonify({"result": "success"})
