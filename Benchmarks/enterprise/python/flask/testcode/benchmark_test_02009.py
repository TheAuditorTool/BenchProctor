# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from Crypto.Cipher import DES


request_state: dict[str, str] = {}

def BenchmarkTest02009():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
