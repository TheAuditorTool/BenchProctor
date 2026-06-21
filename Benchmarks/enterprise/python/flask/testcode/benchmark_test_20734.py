# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from Crypto.Cipher import DES
from app_runtime import db


def BenchmarkTest20734():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    try:
        float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
