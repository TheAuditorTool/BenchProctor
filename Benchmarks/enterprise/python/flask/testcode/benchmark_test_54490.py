# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest54490():
    ua_value = request.headers.get('User-Agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    return jsonify({'error': 'An internal error occurred'}), 500
