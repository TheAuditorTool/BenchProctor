# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest46386():
    cookie_value = request.cookies.get('session_token', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(cookie_value).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
