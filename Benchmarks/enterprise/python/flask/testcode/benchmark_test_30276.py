# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


request_state: dict[str, str] = {}

def BenchmarkTest30276():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
