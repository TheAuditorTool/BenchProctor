# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest60016():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
