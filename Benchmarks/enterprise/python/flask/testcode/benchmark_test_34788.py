# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast


def BenchmarkTest34788(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    return jsonify({'error': 'An internal error occurred'}), 500
