# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31602():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
