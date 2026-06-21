# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
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

async def BenchmarkTest77861(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
