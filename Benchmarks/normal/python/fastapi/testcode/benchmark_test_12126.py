# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
import asyncio


async def BenchmarkTest12126(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
