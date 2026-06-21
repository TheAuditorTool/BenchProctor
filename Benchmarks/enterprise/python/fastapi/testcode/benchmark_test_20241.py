# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


async def BenchmarkTest20241(request: Request):
    ua_value = request.headers.get('user-agent', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(ua_value).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
