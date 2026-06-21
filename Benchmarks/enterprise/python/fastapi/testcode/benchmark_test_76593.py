# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest76593(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
