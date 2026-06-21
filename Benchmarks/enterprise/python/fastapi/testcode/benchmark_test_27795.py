# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest27795(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(cookie_value), secure=True, httponly=True, samesite='Strict')
    return resp
