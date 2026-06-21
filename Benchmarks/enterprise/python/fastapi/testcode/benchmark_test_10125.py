# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest10125(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HTMLResponse(Template(processed).render())
