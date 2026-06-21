# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest24193():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
