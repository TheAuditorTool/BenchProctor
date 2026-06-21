# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest53896(request: Request):
    origin_value = request.headers.get('origin', '')
    data = relay_value(origin_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
