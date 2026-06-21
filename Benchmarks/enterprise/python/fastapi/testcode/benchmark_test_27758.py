# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest27758(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
