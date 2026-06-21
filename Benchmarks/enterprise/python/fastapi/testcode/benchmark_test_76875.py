# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest76875(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
