# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def BenchmarkTest75784():
    auth_header = request.headers.get('Authorization', '')
    requested = str(auth_header) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(auth_header).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
