# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest22529():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    try:
        _bounded = int(data)
        if _bounded < 0 or _bounded > 10000:
            return jsonify({'error': 'out of range'}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
