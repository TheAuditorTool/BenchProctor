# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest02151(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if auth_check('user', str(header_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
