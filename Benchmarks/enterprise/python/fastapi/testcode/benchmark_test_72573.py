# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest72573(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    return HTMLResponse('<!-- diagnostic build token: ' + str(header_value) + ' -->')
