# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest15083(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    request.session.clear()
    request.session['user'] = str(data)
    return {"updated": True}
