# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import urllib.request


async def BenchmarkTest24961(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', forwarded_ip):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = forwarded_ip
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return {"updated": True}
