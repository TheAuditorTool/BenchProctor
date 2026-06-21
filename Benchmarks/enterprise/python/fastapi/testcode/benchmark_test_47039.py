# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest47039(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        granted = auth_check('resource', str(forwarded_ip))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
