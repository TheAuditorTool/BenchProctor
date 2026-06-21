# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest60516(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
