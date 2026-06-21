# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest31652():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
