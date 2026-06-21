# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest22569(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
