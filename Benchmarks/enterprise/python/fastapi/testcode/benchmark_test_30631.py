# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest30631(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    json.loads(data)
    return {"updated": True}
