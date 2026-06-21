# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest66473():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
