# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}

async def BenchmarkTest59959(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
