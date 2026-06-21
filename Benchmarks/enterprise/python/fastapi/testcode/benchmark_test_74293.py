# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest74293(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
