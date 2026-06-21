# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest13888(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
