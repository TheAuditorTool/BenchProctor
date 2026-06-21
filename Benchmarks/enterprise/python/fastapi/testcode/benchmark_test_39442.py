# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest39442(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
