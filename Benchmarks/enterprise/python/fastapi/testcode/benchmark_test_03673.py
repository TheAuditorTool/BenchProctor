# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03673(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
