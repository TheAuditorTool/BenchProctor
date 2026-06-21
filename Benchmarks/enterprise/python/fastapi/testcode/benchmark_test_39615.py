# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest39615(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    return HTMLResponse(str(data))
