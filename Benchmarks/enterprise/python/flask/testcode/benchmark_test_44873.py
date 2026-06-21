# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest44873():
    origin_value = request.headers.get('Origin', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(origin_value), secure=True, httponly=True, samesite='Strict')
    return resp
