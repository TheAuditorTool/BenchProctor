# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from Crypto.Cipher import AES


class UserInput(BaseModel):
    payload: str = ''
def relay_value(value):
    return value

async def BenchmarkTest08020(request: Request, req: UserInput):
    json_value = req.payload
    data = relay_value(json_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
