# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest36167(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
