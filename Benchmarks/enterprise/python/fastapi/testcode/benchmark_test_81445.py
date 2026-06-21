# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
import asyncio


async def BenchmarkTest81445(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
