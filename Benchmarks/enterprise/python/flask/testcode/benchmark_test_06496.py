# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import ast


def BenchmarkTest06496():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    def _primary():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
