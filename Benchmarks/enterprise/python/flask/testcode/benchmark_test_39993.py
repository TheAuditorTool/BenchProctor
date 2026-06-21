# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest39993():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
