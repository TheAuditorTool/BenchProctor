# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import DES
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest12744():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    try:
        int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
