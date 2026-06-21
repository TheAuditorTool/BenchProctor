# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


async def BenchmarkTest73529(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
