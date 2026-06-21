# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


async def BenchmarkTest13244(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
