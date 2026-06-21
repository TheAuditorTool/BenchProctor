# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest75388(path_param):
    path_value = path_param
    data = relay_value(path_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
