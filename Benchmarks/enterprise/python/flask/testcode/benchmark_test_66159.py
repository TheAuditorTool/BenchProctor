# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest66159(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
