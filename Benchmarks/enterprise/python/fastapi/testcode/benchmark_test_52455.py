# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import socket


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest52455(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
