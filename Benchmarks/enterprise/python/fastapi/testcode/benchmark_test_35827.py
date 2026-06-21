# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest35827(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JSONResponse({'action': action}, status_code=200)
