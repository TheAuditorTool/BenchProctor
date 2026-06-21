# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest62134(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
