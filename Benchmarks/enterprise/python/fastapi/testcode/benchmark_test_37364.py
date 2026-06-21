# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest37364(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
