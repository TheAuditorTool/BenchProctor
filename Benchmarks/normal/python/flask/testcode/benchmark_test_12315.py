# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

def BenchmarkTest12315():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
