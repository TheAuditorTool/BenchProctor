# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import DES
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02644():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
