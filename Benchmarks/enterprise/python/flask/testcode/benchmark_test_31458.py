# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31458():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
