# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from Crypto.Cipher import AES
from app_runtime import db


def BenchmarkTest39361():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
