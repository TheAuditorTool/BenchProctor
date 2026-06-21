# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
import base64


async def BenchmarkTest12160(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
