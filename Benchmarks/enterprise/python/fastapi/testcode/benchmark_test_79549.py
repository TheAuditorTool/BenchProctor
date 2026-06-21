# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest79549(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
