# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest44420(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=raw_body))
