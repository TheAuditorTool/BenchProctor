# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest14386():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    processed = data[:64]
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(processed).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
