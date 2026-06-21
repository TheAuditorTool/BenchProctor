# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi import Form


async def BenchmarkTest13731(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
