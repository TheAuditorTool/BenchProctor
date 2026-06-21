# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''
def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest10513(request: Request, req: UserInput):
    json_value = req.payload
    reader = make_reader(json_value)
    data = reader()
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
