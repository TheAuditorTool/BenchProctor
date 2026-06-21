# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest47521(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
