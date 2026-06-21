# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest43354():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
