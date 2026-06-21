# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest01916(request: Request):
    auth_header = request.headers.get('authorization', '')
    if not auth_check(request.session.get('user', ''), str(auth_header)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
