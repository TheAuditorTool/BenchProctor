# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest63525(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
