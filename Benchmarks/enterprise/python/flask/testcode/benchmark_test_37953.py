# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest37953():
    ua_value = request.headers.get('User-Agent', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(ua_value).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
