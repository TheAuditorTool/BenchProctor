# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest20556(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
