# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest05018():
    cookie_value = request.cookies.get('session_token', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(cookie_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
