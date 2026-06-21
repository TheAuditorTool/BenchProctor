# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest80611(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if data != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
