# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest20560(request: Request):
    host_value = request.headers.get('host', '')
    data = RequestPayload(host_value).value
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
