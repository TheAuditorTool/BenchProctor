# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest50506(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
