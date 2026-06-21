# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest74101(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    return HTMLResponse('<div>' + str(data) + '</div>')
