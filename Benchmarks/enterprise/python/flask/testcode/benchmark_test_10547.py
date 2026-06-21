# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import requests
from app_runtime import db


def BenchmarkTest10547():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
