# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest37789(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return {"updated": True}
