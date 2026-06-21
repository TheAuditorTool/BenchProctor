# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest58537(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
