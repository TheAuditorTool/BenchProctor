# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest16276(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
