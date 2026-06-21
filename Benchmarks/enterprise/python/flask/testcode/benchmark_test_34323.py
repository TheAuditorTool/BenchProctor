# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def BenchmarkTest34323():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
