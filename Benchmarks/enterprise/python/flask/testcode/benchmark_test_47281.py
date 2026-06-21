# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import os
import hashlib
from Crypto.Cipher import AES


def BenchmarkTest47281():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return jsonify({'length': len(ciphertext)}), 200
