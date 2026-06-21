# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest57604(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value != request.session.get('csrf_token'):
        return JSONResponse({'error': 'CSRF token mismatch'}, status_code=403)
    if not auth_check(request.session.get('user', ''), str(path_value)):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
