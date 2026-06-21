# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify
import ast


def BenchmarkTest29777():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
