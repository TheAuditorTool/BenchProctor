# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
import asyncio


async def BenchmarkTest79567(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
