# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest00674():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
