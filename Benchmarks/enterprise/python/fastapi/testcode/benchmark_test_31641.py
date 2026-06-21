# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest31641(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
