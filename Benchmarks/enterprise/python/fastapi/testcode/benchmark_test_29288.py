# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest29288(request: Request):
    path_value = request.path_params.get('id', '')
    if auth_check('user', str(path_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
