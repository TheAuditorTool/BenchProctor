# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79343():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
