# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest75392(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    return HTMLResponse(Template(data).render())
