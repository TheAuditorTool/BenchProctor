# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest03218():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return profile_value
    data = asyncio.run(fetch_payload())
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
