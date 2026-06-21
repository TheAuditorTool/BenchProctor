# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest11369(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = default_blank(xml_value)
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
