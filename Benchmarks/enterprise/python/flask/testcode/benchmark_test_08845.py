# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest08845():
    env_value = os.environ.get('USER_INPUT', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(env_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
