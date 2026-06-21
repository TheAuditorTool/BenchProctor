# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from Crypto.Cipher import DES


async def BenchmarkTest71189(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
