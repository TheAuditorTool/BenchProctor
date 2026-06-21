# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest10818(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse('<div>' + str(processed) + '</div>')
