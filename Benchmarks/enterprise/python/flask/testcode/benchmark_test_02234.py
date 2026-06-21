# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest02234():
    raw_body = request.get_data(as_text=True)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(raw_body).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
