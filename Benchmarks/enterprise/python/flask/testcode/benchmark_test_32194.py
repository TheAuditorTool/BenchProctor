# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest32194():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
