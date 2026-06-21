# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import asyncio
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from app_runtime import db


def BenchmarkTest57331():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
