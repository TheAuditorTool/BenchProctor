# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest59193():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
