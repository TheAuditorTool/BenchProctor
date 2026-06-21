# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest63769(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
