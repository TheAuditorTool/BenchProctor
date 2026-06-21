# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest66613(request: Request):
    referer_value = request.headers.get('referer', '')
    if not auth_check(request.session.get('user', ''), str(referer_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
