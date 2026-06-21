# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest57128(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    request.session['data'] = str(forwarded_ip)
    return {"updated": True}
