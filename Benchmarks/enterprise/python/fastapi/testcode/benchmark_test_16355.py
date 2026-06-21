# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest16355(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return HTMLResponse(Template(data).render())
