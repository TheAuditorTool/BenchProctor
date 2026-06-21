# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest15233():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
