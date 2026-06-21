# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
import ast


def BenchmarkTest60186():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    session['data'] = str(data)
    return jsonify({"result": "success"})
