# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest06673():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
