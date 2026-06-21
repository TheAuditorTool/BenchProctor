# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest67490():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
