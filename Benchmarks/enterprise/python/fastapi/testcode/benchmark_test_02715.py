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

async def BenchmarkTest02715(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = RequestPayload(raw_body).value
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
