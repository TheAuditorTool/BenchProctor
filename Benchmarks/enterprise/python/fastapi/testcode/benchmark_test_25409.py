# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest25409(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    return HTMLResponse(Template(header_value).render())
