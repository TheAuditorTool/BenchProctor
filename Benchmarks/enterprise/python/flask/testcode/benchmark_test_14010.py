# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest14010():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    processed = data[:64]
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed))
    return resp
