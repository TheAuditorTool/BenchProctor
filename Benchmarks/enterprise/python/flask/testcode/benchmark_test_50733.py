# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest50733():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
