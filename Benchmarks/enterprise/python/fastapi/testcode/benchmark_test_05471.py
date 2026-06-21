# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


async def BenchmarkTest05471(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
