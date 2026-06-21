# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest13683(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
