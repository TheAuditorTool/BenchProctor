# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
import ast
from app_runtime import auth_check


def BenchmarkTest58408():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
