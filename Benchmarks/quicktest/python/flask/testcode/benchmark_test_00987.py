# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00987():
    ua_value = request.headers.get('User-Agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
