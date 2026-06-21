# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def normalise_input(value):
    return value.strip()

def BenchmarkTest36834():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    try:
        int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
