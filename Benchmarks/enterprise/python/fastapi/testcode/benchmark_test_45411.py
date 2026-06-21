# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import urllib.parse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest45411(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
