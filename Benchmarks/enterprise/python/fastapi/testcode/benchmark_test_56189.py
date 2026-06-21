# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


async def BenchmarkTest56189(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    requested = str(header_value) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(header_value).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
