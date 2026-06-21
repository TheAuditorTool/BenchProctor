# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from Crypto.Cipher import DES


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest20238(request: Request, req: UserInput):
    json_value = req.payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(json_value).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
