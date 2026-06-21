# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest57725(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = default_blank(forwarded_ip)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
