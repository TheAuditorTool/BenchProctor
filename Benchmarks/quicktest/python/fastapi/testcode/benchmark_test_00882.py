# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest00882(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    return HTMLResponse(Template(data).render())
