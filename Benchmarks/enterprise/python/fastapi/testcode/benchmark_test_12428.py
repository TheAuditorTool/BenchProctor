# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest12428(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    return HTMLResponse(Template(data).render())
