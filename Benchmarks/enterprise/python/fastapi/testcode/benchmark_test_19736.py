# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest19736(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
