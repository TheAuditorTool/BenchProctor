# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


request_state: dict[str, str] = {}

async def BenchmarkTest12494(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
