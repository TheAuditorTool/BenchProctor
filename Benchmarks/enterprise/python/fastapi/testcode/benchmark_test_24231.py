# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest24231(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
