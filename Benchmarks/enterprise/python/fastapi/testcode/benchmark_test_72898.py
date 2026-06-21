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

async def BenchmarkTest72898(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    os.system('echo ' + str(data))
    return {"updated": True}
