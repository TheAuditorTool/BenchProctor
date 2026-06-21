# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import urllib.parse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest15565(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
