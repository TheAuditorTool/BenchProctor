# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


async def BenchmarkTest62921(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(raw_body).encode()[:22])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
