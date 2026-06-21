# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


request_state: dict[str, str] = {}

async def BenchmarkTest62802(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
