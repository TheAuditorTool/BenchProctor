# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest29454():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
