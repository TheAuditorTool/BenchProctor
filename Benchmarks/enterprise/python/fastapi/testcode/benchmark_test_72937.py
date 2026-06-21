# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest72937(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
