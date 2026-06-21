# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def BenchmarkTest67386():
    multipart_value = request.form.get('multipart_field', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(multipart_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
