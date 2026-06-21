# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest54886(request: Request):
    host_value = request.headers.get('host', '')
    return HTMLResponse(str(host_value))
