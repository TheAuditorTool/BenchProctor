# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest72416():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
