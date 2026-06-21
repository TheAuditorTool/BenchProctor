# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest41206(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if data != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
