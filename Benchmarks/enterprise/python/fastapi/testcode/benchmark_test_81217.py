# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest81217(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return {"updated": True}
