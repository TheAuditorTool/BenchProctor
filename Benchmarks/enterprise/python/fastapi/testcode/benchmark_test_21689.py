# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest21689(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
