# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def relay_value(value):
    return value

async def BenchmarkTest80704(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(processed)})
