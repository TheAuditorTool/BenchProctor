# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest25798(request: Request, req: UserInput):
    json_value = req.payload
    Fernet(json_value.encode() if isinstance(json_value, str) else json_value).encrypt(b'data')
    return {"updated": True}
