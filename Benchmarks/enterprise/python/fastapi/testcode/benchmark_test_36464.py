# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest36464(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
