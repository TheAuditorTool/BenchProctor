# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


request_state: dict[str, str] = {}

async def BenchmarkTest40156(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'error': str(processed), 'stack': repr(locals())}, status_code=500)
