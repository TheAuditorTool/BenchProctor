# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest66205(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
