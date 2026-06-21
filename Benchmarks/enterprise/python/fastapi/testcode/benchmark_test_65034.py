# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest65034(request: Request):
    auth_header = request.headers.get('authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    if data != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
