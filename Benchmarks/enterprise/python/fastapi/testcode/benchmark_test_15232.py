# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest15232(request: Request):
    ua_value = request.headers.get('user-agent', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(ua_value) + ' -->')
