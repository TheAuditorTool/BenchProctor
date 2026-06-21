# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest11434():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
