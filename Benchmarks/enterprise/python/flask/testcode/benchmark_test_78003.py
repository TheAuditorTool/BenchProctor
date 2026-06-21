# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def ensure_str(value):
    return str(value)

def BenchmarkTest78003():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
