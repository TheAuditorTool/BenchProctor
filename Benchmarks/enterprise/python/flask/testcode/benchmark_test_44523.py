# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest44523():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
