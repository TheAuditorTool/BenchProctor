# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest15449(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
