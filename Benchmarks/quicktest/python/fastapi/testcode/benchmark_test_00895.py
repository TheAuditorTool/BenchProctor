# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest00895(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
