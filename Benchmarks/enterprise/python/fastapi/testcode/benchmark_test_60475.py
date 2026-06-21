# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

async def BenchmarkTest60475(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
