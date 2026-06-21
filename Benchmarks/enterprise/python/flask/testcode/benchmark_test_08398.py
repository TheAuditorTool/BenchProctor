# SPDX-License-Identifier: Apache-2.0
import hashlib
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest08398():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
