# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest25395(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    int(str(data))
    return {"updated": True}
