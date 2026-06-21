# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import base64
from flask import request, jsonify


def BenchmarkTest11350():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
