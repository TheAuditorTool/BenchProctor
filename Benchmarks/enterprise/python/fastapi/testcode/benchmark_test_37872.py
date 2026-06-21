# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


async def BenchmarkTest37872(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(env_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
