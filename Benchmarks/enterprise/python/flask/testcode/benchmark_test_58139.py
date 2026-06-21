# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import ast


def BenchmarkTest58139():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
