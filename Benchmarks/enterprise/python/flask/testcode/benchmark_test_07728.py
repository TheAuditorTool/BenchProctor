# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07728():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
