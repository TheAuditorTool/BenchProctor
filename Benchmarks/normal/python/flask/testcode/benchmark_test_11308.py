# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast


def BenchmarkTest11308(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
