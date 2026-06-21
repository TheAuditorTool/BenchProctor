# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


request_state: dict[str, str] = {}

async def BenchmarkTest76860(request: Request):
    ua_value = request.headers.get('user-agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(processed)})
