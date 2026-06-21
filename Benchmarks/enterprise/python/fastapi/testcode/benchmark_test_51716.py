# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import re
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest51716(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return {"updated": True}
