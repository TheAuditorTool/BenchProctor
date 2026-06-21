# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest55602():
    referer_value = request.headers.get('Referer', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(referer_value), secure=True, httponly=True, samesite='Strict')
    return resp
