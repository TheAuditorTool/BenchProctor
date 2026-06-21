# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest22356(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
