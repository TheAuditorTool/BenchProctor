# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest32326(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
