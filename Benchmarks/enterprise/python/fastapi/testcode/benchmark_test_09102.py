# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest09102(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
