# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time
import ast


def BenchmarkTest42234(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
