# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest24936(request: Request):
    referer_value = request.headers.get('referer', '')
    data = RequestPayload(referer_value).value
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
