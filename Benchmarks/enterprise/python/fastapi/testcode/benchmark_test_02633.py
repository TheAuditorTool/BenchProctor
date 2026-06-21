# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi import Form


async def BenchmarkTest02633(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
