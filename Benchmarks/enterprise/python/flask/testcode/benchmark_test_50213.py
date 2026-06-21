# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.Cipher import DES


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest50213():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
