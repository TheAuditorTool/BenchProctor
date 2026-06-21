# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03628():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return jsonify({'error': 'forbidden'}), 403
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
