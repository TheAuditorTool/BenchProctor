# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest15726(request: Request):
    ua_value = request.headers.get('user-agent', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(ua_value))
    return resp
