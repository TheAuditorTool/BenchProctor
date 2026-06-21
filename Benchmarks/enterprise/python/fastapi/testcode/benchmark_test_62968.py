# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest62968(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
