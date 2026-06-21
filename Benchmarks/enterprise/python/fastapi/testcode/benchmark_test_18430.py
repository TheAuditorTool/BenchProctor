# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest18430(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    return HTMLResponse('<script src="' + str(data) + '"></script>')
