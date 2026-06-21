# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest45479(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
