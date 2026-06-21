# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest34088(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
