# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest19426(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
