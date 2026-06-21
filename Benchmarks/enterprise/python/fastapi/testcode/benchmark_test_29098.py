# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest29098(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
