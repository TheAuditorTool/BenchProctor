# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest52114(request: Request):
    query_array = request.query_params.get('items', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return query_array
    data = await fetch_payload()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
