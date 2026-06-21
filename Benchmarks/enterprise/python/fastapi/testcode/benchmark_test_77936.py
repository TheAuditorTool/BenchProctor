# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest77936(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
