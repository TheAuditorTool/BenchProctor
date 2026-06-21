# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest53185(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
