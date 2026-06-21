# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from Crypto.Cipher import DES


async def BenchmarkTest09819(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    if str(data).lower() not in ('true', 'false'):
        return JSONResponse({'error': 'invalid boolean'}, status_code=400)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
