# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def normalise_input(value):
    return value.strip()

def BenchmarkTest34704():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
