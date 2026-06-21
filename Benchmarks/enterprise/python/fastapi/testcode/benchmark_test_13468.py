# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest13468(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = False
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
