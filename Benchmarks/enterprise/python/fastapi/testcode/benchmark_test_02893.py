# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import asyncio
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


async def BenchmarkTest02893(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
