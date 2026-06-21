# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


def to_text(value):
    return str(value).strip()

async def BenchmarkTest04940(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
