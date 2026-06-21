# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest10034():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return jsonify({'error': 'forbidden'}), 403
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
