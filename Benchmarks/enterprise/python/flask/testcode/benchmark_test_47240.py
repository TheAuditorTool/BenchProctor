# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest47240():
    auth_header = request.headers.get('Authorization', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(auth_header), secure=True, httponly=True, samesite='Strict')
    return resp
