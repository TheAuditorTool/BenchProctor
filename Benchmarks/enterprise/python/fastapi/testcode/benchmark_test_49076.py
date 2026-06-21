# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
import hashlib
from Crypto.Cipher import AES


def to_text(value):
    return str(value).strip()

async def BenchmarkTest49076(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
