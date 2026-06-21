# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest11565(request: Request):
    host_value = request.headers.get('host', '')
    return HTMLResponse(Template(host_value).render())
