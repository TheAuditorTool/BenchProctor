# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest56544(request: Request):
    host_value = request.headers.get('host', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(host_value), secure=True, httponly=True, samesite='Strict')
    return resp
