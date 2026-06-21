# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest75182(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
