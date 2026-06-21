# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import ast


def BenchmarkTest55985(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
