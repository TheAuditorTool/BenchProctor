# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest73110(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    globals()['counter'] = int(data)
    return {"updated": True}
