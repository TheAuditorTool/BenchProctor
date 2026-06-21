# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest12855(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
