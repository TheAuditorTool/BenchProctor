# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest00600(request: Request):
    referer_value = request.headers.get('referer', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(referer_value) + ' -->')
