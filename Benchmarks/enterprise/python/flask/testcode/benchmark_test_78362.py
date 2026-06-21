# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import ast


def BenchmarkTest78362():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
