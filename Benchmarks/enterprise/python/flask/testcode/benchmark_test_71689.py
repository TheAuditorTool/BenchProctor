# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest71689():
    auth_header = request.headers.get('Authorization', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(auth_header).encode())
    return jsonify({'length': len(ciphertext)}), 200
