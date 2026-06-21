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

async def BenchmarkTest37245(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
