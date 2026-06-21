# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest63983(request: Request):
    origin_value = request.headers.get('origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
