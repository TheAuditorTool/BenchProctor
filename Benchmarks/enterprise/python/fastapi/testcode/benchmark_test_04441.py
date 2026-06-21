# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os
import hashlib
from Crypto.Cipher import AES


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04441(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
