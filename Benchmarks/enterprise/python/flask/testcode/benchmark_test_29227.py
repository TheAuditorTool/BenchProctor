# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest29227(path_param):
    path_value = path_param
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(path_value), secure=True, httponly=True, samesite='Strict')
    return resp
