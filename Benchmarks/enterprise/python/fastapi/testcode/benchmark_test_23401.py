# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest23401(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    if data != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
