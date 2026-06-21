# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest37348():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
