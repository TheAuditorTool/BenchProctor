# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12429(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
