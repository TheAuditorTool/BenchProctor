# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


request_state: dict[str, str] = {}

def BenchmarkTest20443(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
