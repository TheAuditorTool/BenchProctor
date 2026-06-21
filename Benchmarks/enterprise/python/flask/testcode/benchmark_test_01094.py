# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def BenchmarkTest01094():
    upload_name = request.files['upload'].filename
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(upload_name).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
