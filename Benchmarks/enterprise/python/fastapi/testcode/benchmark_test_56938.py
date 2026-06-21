# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest56938(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
