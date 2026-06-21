# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
import ctypes


async def BenchmarkTest12484(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
