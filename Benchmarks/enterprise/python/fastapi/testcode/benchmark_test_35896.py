# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


async def BenchmarkTest35896(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
