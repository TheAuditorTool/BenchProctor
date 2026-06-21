# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from Crypto.Cipher import DES
from app_runtime import db


def BenchmarkTest69722():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    try:
        float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200
