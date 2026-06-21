# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from Crypto.Cipher import AES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest61755():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
