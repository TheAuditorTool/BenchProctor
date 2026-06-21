# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest05477(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
