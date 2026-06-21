# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest01119(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    return HTMLResponse(Template(data).render())
