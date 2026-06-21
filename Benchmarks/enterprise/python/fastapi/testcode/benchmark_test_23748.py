# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest23748(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
