# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest21613(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
