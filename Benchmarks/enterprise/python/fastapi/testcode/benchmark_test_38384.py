# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import base64
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest38384(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
