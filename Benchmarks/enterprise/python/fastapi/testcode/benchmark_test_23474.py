# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest23474(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ctx = RequestContext(profile_value)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
