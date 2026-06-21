# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest11365(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if auth_check('user', str(forwarded_ip)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
