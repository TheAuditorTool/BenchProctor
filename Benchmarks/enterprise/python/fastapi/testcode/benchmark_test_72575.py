# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest72575(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = default_blank(multipart_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
