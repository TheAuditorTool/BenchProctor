# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest65008():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
