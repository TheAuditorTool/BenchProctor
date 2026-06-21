# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from flask import session


def BenchmarkTest37539():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
