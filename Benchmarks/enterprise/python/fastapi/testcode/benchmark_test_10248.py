# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest10248(request: Request):
    path_value = request.path_params.get('id', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(path_value), secure=True, httponly=True, samesite='Strict')
    return resp
