# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest44500(request: Request):
    origin_value = request.headers.get('origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
