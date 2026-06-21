# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest47774(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not auth_check(request.session.get('user', ''), str(forwarded_ip)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
