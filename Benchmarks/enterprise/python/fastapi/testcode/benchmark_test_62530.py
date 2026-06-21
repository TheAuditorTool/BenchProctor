# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest62530(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not auth_check(str(forwarded_ip), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
