# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest00440(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
