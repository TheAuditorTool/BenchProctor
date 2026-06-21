# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest08231():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
