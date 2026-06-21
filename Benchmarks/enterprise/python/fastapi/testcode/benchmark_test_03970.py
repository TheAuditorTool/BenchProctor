# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
import re


async def BenchmarkTest03970(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
