# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest18388(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
