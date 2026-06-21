# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import AES
from app_runtime import db


def BenchmarkTest04135():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
