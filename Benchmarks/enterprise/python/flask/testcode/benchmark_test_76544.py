# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest76544():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    session['data'] = str(processed)
    return jsonify({"result": "success"})
