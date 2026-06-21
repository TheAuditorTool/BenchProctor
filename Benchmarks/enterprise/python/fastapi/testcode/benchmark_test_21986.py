# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest21986(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    requested = str(data) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
