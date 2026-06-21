# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def BenchmarkTest07319():
    ua_value = request.headers.get('User-Agent', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(ua_value).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
