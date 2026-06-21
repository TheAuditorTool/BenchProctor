# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest23560(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
