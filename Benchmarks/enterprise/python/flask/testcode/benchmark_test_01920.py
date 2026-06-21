# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import hashlib
from Crypto.Cipher import AES


def BenchmarkTest01920(path_param):
    path_value = path_param
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(path_value).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return jsonify({'length': len(ciphertext)}), 200
