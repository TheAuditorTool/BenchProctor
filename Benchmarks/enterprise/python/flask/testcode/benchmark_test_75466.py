# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest75466():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
