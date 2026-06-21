# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest69538():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
