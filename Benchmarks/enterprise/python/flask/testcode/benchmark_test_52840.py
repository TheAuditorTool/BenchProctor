# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import asyncio
from app_runtime import db, auth_check


def BenchmarkTest52840():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
