# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest28169(request: Request):
    origin_value = request.headers.get('origin', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(origin_value), secure=True, httponly=True, samesite='Strict')
    return resp
