# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest75523(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
