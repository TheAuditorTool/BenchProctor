# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os
import hashlib
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

def BenchmarkTest62209():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return jsonify({'length': len(ciphertext)}), 200
