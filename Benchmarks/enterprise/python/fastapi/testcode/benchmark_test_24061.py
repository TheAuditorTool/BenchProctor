# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest24061(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
