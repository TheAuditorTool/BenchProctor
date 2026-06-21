# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest48483(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
