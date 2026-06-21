# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import ast


def BenchmarkTest05809():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
