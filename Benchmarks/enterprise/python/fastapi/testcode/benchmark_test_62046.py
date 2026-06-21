# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest62046(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
