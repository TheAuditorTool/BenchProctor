# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79747():
    field_value = request.form.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
