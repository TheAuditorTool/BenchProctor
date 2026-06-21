# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest07798(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
