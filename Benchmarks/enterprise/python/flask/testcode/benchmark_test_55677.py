# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest55677():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
