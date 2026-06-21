# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest06894(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(raw_body), secure=True, httponly=True, samesite='Strict')
    return resp
