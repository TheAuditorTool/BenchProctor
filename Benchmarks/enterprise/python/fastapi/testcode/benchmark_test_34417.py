# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest34417(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = coalesce_blank(upload_name)
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=data))
