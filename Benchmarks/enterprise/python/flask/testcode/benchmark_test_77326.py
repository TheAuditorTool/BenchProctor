# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
import requests


def BenchmarkTest77326():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
