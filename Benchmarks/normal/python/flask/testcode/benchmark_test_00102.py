# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import hashlib
from Crypto.Cipher import AES


def BenchmarkTest00102():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return jsonify({'length': len(ciphertext)}), 200
