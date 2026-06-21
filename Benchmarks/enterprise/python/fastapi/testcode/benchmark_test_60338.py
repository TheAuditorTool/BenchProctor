# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

async def BenchmarkTest60338(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    requested = str(data) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
