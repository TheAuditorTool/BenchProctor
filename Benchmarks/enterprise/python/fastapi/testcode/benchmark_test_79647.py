# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest79647(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    return HTMLResponse(Template(data).render())
