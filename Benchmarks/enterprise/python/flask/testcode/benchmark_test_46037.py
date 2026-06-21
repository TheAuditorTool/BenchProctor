# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import DES
from app_runtime import db


def BenchmarkTest46037():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(comment_value).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
