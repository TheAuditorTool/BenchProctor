# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest72940(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
