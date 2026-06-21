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

async def BenchmarkTest63527(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = RequestPayload(forwarded_ip).value
    return HTMLResponse(Template(data).render())
