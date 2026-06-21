# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os
import ast


def BenchmarkTest68565():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
