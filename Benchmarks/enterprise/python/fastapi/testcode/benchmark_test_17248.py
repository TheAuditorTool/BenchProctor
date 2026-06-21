# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest17248(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    if str(data) == 'fluffy':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
