# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi import Form


async def BenchmarkTest74321(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
