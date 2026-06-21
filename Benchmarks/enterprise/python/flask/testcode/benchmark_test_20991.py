# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest20991():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
