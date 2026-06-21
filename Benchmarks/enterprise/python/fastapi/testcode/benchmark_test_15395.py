# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest15395(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
