# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest11419(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if not auth_check(request.session.get('user', ''), str(env_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
