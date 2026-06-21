# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest60693():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
