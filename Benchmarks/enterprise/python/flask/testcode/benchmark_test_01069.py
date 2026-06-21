# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01069():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
