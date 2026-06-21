# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest26629(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
