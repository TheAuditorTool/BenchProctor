# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest22520(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
