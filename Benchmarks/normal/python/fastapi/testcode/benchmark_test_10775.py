# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest10775(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
