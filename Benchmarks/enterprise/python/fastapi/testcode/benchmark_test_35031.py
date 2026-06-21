# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest35031(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
