# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from Crypto.Cipher import DES


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest58859():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
