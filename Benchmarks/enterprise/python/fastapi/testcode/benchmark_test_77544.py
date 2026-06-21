# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest77544(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
