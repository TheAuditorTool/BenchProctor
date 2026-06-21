# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest80293(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not auth_check(request.session.get('user', ''), str(header_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
