# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest59065(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
