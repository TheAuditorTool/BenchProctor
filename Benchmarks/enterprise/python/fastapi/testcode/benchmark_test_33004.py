# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest33004(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    result = 100 / int(str(data))
    return {"updated": True}
