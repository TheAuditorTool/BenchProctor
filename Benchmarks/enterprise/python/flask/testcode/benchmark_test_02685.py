# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest02685():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
