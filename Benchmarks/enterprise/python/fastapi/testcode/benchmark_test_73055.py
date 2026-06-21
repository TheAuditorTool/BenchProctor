# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


async def BenchmarkTest73055(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(multipart_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
