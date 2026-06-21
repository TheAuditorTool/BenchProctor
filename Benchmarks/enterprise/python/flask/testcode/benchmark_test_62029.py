# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import asyncio
from app_runtime import db


def BenchmarkTest62029():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
