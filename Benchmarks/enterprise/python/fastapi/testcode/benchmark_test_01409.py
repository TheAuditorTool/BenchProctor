# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest01409(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if auth_check('user', str(cookie_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
