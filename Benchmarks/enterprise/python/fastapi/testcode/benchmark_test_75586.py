# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest75586(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
