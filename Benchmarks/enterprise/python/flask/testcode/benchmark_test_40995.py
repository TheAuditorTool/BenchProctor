# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest40995():
    env_value = os.environ.get('USER_INPUT', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(env_value).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
