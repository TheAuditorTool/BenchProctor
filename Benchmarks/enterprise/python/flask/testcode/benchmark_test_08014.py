# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest08014():
    host_value = request.headers.get('Host', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(host_value), secure=True, httponly=True, samesite='Strict')
    return resp
