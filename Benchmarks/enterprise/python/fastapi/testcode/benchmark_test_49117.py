# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest49117(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    result = 100 / int(str(data))
    return {"updated": True}
