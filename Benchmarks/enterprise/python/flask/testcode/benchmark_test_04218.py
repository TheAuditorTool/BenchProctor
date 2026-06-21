# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest04218():
    auth_header = request.headers.get('Authorization', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(auth_header).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
