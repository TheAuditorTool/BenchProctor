# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest69905(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
