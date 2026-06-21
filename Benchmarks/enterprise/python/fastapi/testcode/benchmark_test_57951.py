# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest57951(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
