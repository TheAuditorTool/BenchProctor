# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest54109(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
