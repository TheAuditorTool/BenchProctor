# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast


def BenchmarkTest01027(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
