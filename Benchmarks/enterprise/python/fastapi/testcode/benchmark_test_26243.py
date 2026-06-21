# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest26243(request: Request):
    user_id = request.query_params.get('id', '')
    data = default_blank(user_id)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
