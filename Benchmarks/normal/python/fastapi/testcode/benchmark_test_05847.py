# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest05847(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    request.session.clear()
    request.session['user'] = str(data)
    return {"updated": True}
