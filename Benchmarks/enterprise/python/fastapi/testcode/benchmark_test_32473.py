# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest32473(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
