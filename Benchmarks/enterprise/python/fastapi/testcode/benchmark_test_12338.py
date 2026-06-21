# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


def to_text(value):
    return str(value).strip()

async def BenchmarkTest12338(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
