# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest02936(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
