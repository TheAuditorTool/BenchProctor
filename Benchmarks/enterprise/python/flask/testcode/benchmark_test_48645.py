# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest48645(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
