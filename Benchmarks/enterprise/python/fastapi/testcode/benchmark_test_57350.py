# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest57350(request: Request):
    referer_value = request.headers.get('referer', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(referer_value), secure=True, httponly=True, samesite='Strict')
    return resp
