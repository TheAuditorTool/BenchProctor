# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest39191(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
