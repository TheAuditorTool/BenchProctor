# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from app_runtime import db


def BenchmarkTest02775():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200
