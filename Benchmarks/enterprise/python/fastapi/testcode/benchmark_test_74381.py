# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest74381(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
