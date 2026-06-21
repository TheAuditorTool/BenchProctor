# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import ast


def BenchmarkTest51606(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
