# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest23600():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
