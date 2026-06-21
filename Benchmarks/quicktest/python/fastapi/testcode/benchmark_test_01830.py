# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi import Form


async def BenchmarkTest01830(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
