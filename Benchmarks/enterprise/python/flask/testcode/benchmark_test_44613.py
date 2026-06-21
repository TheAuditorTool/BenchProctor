# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest44613():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
