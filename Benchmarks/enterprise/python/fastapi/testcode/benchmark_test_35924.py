# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest35924(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return HTMLResponse(str(data))
