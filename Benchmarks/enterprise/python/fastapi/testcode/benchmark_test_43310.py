# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest43310(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(env_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
