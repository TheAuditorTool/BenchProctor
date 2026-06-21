# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02100():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
