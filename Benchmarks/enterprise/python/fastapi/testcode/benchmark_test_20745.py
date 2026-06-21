# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest20745(request: Request):
    origin_value = request.headers.get('origin', '')
    if not auth_check(request.session.get('user', ''), str(origin_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
