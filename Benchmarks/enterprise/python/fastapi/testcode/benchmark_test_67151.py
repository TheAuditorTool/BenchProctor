# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest67151(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
