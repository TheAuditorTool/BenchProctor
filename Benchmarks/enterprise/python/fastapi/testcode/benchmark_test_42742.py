# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


request_state: dict[str, str] = {}

async def BenchmarkTest42742(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
