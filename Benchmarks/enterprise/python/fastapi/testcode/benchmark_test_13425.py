# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest13425(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ensure_str(referer_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
