# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


request_state: dict[str, str] = {}

async def BenchmarkTest58447(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
