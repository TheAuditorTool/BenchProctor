# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
import ast


def BenchmarkTest50646():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
