# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest11833(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
