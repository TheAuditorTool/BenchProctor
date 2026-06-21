# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest50756(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
