# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest03557(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    if not auth_check(request.session.get('user', ''), str(env_value)):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
