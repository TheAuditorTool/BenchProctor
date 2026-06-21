# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59215():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
