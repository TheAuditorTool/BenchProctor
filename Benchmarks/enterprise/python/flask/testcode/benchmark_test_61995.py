# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest61995():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
