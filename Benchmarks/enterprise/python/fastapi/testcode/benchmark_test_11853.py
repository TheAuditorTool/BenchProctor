# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11853(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
