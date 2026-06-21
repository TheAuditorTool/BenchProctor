# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest38471(request: Request):
    host_value = request.headers.get('host', '')
    data = default_blank(host_value)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
