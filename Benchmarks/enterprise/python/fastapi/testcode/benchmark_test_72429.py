# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest72429(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not auth_check('user', hashlib.sha256(str(forwarded_ip).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
