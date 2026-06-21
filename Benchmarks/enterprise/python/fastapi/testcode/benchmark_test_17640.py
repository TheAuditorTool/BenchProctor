# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest17640(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
