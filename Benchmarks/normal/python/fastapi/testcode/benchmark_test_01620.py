# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import html
import os
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest01620(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    processed = str(data).replace("<script", "")
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
