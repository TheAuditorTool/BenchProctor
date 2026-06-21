# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest05925(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
