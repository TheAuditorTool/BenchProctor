# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest00301(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return HTMLResponse(Template(data).render())
