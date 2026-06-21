# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest30066():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    return jsonify({'error': 'An internal error occurred'}), 500
