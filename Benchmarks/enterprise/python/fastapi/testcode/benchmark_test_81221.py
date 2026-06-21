# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest81221(request: Request, req: UserInput):
    json_value = req.payload
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(json_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
