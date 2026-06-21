# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest25702():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
