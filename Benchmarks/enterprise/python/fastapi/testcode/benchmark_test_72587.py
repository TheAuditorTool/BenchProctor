# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest72587(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
