# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest18747(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
