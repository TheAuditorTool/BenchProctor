# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest46990(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
