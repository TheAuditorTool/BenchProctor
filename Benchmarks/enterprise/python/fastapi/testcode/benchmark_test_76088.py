# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest76088(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JSONResponse({'action': action}, status_code=200)
