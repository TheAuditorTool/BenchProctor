# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest06200(request: Request):
    host_value = request.headers.get('host', '')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(host_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
