# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from Crypto.Cipher import DES
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest68283():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
