# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
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

async def BenchmarkTest53951(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    auth_check('user', data)
    return {"updated": True}
