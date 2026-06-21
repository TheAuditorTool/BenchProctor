# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest14540(request: Request):
    referer_value = request.headers.get('referer', '')
    if not auth_check('user', hashlib.sha256(str(referer_value).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
