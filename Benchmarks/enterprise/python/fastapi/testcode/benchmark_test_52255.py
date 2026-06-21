# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from Crypto.Cipher import DES


async def BenchmarkTest52255(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    processed = data[:64]
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
