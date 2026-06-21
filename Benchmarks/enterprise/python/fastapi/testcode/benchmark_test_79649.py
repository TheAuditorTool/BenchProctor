# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest79649(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
