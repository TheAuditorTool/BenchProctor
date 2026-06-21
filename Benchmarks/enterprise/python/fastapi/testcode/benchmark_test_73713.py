# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os
from starlette.responses import HTMLResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest73713(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
