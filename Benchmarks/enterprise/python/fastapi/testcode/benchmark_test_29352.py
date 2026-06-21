# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest29352(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
