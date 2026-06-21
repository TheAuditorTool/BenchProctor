# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest33946():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
