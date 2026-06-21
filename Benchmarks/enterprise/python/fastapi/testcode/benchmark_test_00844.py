# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest00844(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if not auth_check(request.session.get('user', ''), str(cookie_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
