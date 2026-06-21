# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest34060():
    cookie_value = request.cookies.get('session_token', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(cookie_value).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
