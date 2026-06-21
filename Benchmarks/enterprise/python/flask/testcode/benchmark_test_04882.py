# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest04882():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
