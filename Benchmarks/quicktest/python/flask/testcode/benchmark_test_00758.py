# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest00758():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
