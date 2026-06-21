# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import json
import os
import hashlib
from Crypto.Cipher import AES


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06899(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
