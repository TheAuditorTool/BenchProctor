# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest10133(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
