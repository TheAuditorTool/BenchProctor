# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest64441(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    return HTMLResponse(Template(data).render())
