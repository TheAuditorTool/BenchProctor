# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest52564(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
