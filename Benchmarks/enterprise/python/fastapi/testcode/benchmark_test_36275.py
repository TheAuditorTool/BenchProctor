# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


async def BenchmarkTest36275(request: Request):
    host_value = request.headers.get('host', '')
    requested = str(host_value) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(host_value).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
