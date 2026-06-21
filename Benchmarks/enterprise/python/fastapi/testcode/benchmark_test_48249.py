# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest48249(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if not auth_check(request.session.get('user', ''), str(ua_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
