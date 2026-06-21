# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
import ast


def BenchmarkTest63173(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    session['data'] = str(data)
    return jsonify({"result": "success"})
