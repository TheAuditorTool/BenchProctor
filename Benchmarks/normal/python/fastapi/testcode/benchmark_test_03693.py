# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest03693(request: Request):
    auth_header = request.headers.get('authorization', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(auth_header), secure=True, httponly=True, samesite='Strict')
    return resp
