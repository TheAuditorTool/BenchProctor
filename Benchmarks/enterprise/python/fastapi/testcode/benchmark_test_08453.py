# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest08453(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
