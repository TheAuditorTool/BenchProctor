# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest56786():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    processed = data[:64]
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(processed).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
