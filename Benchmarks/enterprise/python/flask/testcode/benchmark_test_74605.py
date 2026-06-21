# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import ast


def BenchmarkTest74605(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
