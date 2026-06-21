# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import ast


def BenchmarkTest08639():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
