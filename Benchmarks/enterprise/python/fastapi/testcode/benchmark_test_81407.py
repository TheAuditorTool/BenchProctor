# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest81407(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
