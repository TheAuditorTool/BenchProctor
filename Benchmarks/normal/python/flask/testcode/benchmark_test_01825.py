# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def coalesce_blank(value):
    return value or ''

def BenchmarkTest01825():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
