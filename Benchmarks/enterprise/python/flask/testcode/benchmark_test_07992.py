# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast


def BenchmarkTest07992(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
