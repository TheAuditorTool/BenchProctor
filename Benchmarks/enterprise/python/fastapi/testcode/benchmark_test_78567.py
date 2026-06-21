# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


async def BenchmarkTest78567(request: Request):
    auth_header = request.headers.get('authorization', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(auth_header).encode()[:22])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
