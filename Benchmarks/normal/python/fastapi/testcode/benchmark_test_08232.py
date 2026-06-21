# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest08232(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
