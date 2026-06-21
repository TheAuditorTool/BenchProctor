# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest19006(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
