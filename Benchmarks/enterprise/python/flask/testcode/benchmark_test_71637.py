# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest71637(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
