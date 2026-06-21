# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest10103(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_check('user', str(auth_header)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
