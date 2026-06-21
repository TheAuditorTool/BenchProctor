# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest40809(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
