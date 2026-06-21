# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest15768(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
