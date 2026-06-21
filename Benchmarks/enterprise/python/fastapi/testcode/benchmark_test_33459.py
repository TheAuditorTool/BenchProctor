# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest33459(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
