# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest11781(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
