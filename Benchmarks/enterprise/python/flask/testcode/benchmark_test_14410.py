# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def BenchmarkTest14410():
    referer_value = request.headers.get('Referer', '')
    requested = str(referer_value) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(referer_value).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200
