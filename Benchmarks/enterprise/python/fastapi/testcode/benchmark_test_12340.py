# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest12340(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
