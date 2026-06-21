# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest19410(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    return JSONResponse({'error': str(cookie_value), 'stack': repr(locals())}, status_code=500)
