# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest04159(request: Request):
    path_value = request.path_params.get('id', '')
    data = coalesce_blank(path_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
