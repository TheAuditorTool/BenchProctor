# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest26383(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ctx = RequestContext(upload_name)
    data = ctx.payload
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
