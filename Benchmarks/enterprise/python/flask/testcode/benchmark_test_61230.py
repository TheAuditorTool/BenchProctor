# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os
import ast


def BenchmarkTest61230():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
