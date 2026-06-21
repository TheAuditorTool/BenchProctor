# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest60689():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
