# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify
import ast


def BenchmarkTest07872(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
