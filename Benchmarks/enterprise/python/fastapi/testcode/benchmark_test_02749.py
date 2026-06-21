# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest02749(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
