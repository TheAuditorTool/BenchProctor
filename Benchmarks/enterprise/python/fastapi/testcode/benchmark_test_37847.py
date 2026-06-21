# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest37847(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    async def _evasion_task():
        requests.get(str(data))
    await _evasion_task()
    return {"updated": True}
