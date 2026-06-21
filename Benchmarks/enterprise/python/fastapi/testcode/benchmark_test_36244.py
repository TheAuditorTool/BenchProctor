# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest36244(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
