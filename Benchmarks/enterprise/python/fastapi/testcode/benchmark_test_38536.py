# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest38536(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JSONResponse({'action': action}, status_code=200)
