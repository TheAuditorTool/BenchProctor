# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest39379():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    return str(data), 200, {'Content-Type': 'text/html'}
