# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}

async def BenchmarkTest22579(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return {"updated": True}
