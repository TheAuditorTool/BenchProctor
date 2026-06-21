# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest01507(request: Request):
    host_value = request.headers.get('host', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(host_value) + ' -->')
