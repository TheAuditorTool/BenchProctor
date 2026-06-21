# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


async def BenchmarkTest78265(request: Request):
    referer_value = request.headers.get('referer', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(referer_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
