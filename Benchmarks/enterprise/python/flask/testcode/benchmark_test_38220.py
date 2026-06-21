# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest38220():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
