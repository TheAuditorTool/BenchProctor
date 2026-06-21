# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest36717():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    return jsonify({'error': 'An internal error occurred'}), 500
