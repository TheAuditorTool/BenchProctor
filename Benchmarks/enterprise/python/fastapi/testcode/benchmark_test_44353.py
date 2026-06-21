# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


async def BenchmarkTest44353(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(env_value).encode()[:22])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
