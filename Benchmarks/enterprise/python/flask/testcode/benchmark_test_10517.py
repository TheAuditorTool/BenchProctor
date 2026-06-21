# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest10517():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
