# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12538(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(forwarded_ip))
    return resp
