# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest10342():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
