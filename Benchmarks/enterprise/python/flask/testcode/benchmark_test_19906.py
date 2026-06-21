# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest19906():
    auth_header = request.headers.get('Authorization', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(auth_header).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
