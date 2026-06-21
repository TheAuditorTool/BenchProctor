# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.Cipher import DES


def BenchmarkTest04807():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
