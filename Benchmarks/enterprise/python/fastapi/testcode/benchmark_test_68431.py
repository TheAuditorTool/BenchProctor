# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest68431(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    globals()['counter'] = int(data)
    return {"updated": True}
