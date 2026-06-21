# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


async def BenchmarkTest56310(request: Request):
    upload_name = (await request.form()).get('upload', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(upload_name).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
