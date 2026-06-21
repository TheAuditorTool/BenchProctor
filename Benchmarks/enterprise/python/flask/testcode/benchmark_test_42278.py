# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.Cipher import AES


def BenchmarkTest42278():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
