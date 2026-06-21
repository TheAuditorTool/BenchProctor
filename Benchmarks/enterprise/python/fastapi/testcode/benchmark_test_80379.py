# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import asyncio
import urllib.parse


async def BenchmarkTest80379(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
