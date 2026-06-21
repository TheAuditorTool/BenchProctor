# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59957():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
