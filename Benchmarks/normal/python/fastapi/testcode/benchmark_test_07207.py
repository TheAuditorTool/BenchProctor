# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest07207(request: Request):
    auth_header = request.headers.get('authorization', '')
    return HTMLResponse(Template(auth_header).render())
