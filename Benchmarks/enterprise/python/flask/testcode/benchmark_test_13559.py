# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13559():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
