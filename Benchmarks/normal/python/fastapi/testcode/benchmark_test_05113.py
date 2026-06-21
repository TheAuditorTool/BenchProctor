# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from fastapi import Form


async def BenchmarkTest05113(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    return HTMLResponse(Template(data).render())
