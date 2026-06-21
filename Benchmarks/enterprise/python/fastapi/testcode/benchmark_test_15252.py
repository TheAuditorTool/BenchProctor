# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest15252(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
