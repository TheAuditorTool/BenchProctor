# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest44609(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = default_blank(forwarded_ip)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
