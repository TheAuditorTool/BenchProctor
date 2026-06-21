# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest20059(request: Request):
    path_value = request.path_params.get('id', '')
    if not auth_check(request.session.get('user', ''), str(path_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
