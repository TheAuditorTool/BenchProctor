# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest07958(request: Request, req: UserInput):
    json_value = req.payload
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
