# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest50519(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
