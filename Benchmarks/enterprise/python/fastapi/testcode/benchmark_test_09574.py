# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest09574(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    processed = str(data).replace("<script", "")
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
