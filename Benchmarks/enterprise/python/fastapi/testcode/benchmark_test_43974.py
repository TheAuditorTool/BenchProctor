# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest43974(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
