# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest65875():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    return str(data), 200, {'Content-Type': 'text/html'}
