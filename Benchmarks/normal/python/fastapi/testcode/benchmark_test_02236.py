# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest02236(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
