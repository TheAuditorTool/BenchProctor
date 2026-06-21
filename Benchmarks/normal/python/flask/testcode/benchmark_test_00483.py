# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import hashlib
from Crypto.Cipher import AES


def BenchmarkTest00483():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(json_value).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return jsonify({'length': len(ciphertext)}), 200
