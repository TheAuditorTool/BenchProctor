# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest03368(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
