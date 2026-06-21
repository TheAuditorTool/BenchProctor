# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest13394(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
