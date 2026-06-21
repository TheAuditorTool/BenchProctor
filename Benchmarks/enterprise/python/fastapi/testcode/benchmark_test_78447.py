# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest78447(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
