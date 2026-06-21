# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

async def BenchmarkTest43773(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
