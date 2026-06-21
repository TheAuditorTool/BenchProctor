# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest74066():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
