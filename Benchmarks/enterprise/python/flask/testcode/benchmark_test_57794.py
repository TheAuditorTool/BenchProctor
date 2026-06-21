# SPDX-License-Identifier: Apache-2.0
from flask import request
import ast


def BenchmarkTest57794():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    return str(data), 200, {'Content-Type': 'text/html'}
