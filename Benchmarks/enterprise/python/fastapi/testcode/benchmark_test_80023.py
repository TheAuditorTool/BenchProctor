# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest80023(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    return HTMLResponse(str(data))
