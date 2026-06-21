# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest02916(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
