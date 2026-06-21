# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify
import ast


def BenchmarkTest18189():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
