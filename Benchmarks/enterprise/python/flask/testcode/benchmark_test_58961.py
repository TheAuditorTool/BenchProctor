# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest58961():
    ua_value = request.headers.get('User-Agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
